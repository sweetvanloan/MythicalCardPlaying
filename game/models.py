from dataclasses import dataclass, field
from typing import List, Optional, Dict, Callable
from .types import Type

@dataclass(frozen=True)
class Attack:
    name: str
    damage: int

# Enhancements are simple passive modifiers for this version.
# Supported modifier keys:
#   - "attack_bonus_by_type": Dict[Type, int]  -> +X dmg if attacker is that Type
#   - "flat_damage_reduction": int             -> reduce incoming damage by X (min 0)
@dataclass(frozen=True)
class EnhancementCard:
    name: str
    text: str
    modifiers: Dict[str, object] = field(default_factory=dict)

@dataclass
class CreatureCard:
    name: str
    ctype: Type
    max_hp: int
    attacks: List[Attack]

    # runtime hp (set when the creature enters play)
    hp: int = field(init=False)

    def __post_init__(self):
        object.__setattr__(self, "hp", self.max_hp)

@dataclass
class PlayerState:
    name: str
    deck: List[object] = field(default_factory=list)  # CreatureCard | EnhancementCard
    hand: List[object] = field(default_factory=list)
    board_enhancements: List[EnhancementCard] = field(default_factory=list)
    active_creature: Optional[CreatureCard] = None

    def draw(self, n: int = 1):
        for _ in range(n):
            if not self.deck:  # no card to draw, do nothing (or fatigue rules later)
                return
            self.hand.append(self.deck.pop(0))

    def play_first_enhancement(self):
        for i, card in enumerate(self.hand):
            if isinstance(card, EnhancementCard):
                enh = self.hand.pop(i)
                self.board_enhancements.append(enh)
                return enh
        return None

    def play_first_creature(self):
        if self.active_creature is not None:
            return None
        for i, card in enumerate(self.hand):
            if isinstance(card, CreatureCard):
                creature: CreatureCard = self.hand.pop(i)
                # fresh HP when entering
                creature.hp = creature.max_hp  # type: ignore[attr-defined]
                self.active_creature = creature
                return creature
        return None
