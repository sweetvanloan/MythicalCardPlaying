from dataclasses import dataclass, field
from typing import List, Optional
import random

from .types import Phase, Type
from .models import PlayerState, CreatureCard, EnhancementCard, Attack
from .data import build_deck

@dataclass
class GameState:
    players: List[PlayerState]
    rng: random.Random = field(default_factory=lambda: random.Random(42))
    phase: Phase = Phase.DRAW
    active_player_idx: int = 0

    def next_phase(self):
        order = {Phase.DRAW: Phase.MAIN, Phase.MAIN: Phase.ATTACK, Phase.ATTACK: Phase.END, Phase.END: Phase.DRAW}
        self.phase = order[self.phase]
        if self.phase == Phase.DRAW:
            self.active_player_idx = (self.active_player_idx + 1) % len(self.players)

    @property
    def active_player(self) -> PlayerState:
        return self.players[self.active_player_idx]

def start_game(num_players: int = 2, seed: int = 42) -> GameState:
    rng = random.Random(seed)
    players = [PlayerState(name=f"Player {i+1}") for i in range(num_players)]
    for p in players:
        p.deck = build_deck(rng)
        p.draw(5)
        p.play_first_enhancement()
        p.play_first_creature()
    return GameState(players=players, rng=rng)

def compute_attack_damage(attacker: PlayerState, defender: PlayerState, atk_card: CreatureCard, attack: Attack) -> int:
    dmg = attack.damage

    # Apply attack bonuses from attacker's enhancements
    for enh in attacker.board_enhancements:
        bonus_map = enh.modifiers.get("attack_bonus_by_type")
        if isinstance(bonus_map, dict):
            bonus = bonus_map.get(atk_card.ctype, 0)
            dmg += bonus

    # Apply flat damage reduction from defender's enhancements
    reduction_total = 0
    for enh in defender.board_enhancements:
        red = enh.modifiers.get("flat_damage_reduction", 0)
        if isinstance(red, int):
            reduction_total += red

    dmg = max(0, dmg - reduction_total)
    return dmg

def attack_target(state: GameState, attacker_idx: int, defender_idx: int):
    atk_player = state.players[attacker_idx]
    def_player = state.players[defender_idx]
    atk_card = atk_player.active_creature
    def_card = def_player.active_creature

    if not atk_card or not def_card:
        return "No valid battle (missing active creature)."

    # Choose attack (simple AI: pick highest damage)
    attack = max(atk_card.attacks, key=lambda a: a.damage) if atk_card.attacks else None
    if attack is None:
        return f"{atk_player.name}'s {atk_card.name} cannot attack."

    dmg = compute_attack_damage(atk_player, def_player, atk_card, attack)
    def_card.hp = max(0, def_card.hp - dmg)

    log = f"{atk_player.name}'s {atk_card.name} uses {attack.name} for {dmg} damage → {def_player.name}'s {def_card.name} (HP {def_card.hp}/{def_card.max_hp})"
    if def_card.hp == 0:
        def_player.active_creature = None
        log += f" — {def_player.name}'s {def_card.name} is knocked out!"
    return log

def round_robin_battles(state: GameState) -> List[str]:
    """Each player attacks the next player once (P1→P2, P2→P3, ..., Pn→P1)."""
    logs: List[str] = []
    n = len(state.players)
    for i in range(n):
        j = (i + 1) % n
        logs.append(attack_target(state, i, j))
    return logs
