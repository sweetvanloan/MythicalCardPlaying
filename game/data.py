import random
from typing import List
from .types import Type
from .models import CreatureCard, EnhancementCard, Attack

def base_creatures() -> List[CreatureCard]:
    # Each has 2–3 attacks, a Type, and HP.
    return [
        CreatureCard("Phoenix",   Type.FIRE,  18, [Attack("Flame Wing", 7), Attack("Fire Blast", 5)]),
        CreatureCard("Leviathan", Type.WATER, 22, [Attack("Tidal Wave", 8), Attack("Aqua Slam", 6)]),
        CreatureCard("Dracula",   Type.DARK,  16, [Attack("Vampiric Bite", 7), Attack("Shadow Strike", 6)]),
        CreatureCard("Goliath",   Type.EARTH, 20, [Attack("Stone Throw", 6), Attack("Earthquake", 7)]),
        CreatureCard("Kraken",    Type.WATER, 24, [Attack("Whirlpool", 8), Attack("Tentacle Crush", 7)]),
        CreatureCard("Dragon",    Type.FIRE,  22, [Attack("Fire Breath", 9), Attack("Tail Swipe", 6)]),
        CreatureCard("Unicorn",   Type.LIGHT, 18, [Attack("Horn Charge", 6), Attack("Healing Light", 0)]),
        CreatureCard("Wizard",    Type.ARCANE,16, [Attack("Magic Missile", 5), Attack("Arcane Blast", 7)]),
        CreatureCard("Werewolf",  Type.DARK,  19, [Attack("Lunar Strike", 7), Attack("Feral Claw", 6)]),
        CreatureCard("Poltergeist",Type.SPIRIT,15,[Attack("Eerie Wail", 6), Attack("Haunting Chill", 5)]),
        CreatureCard("Kitsune",   Type.MYSTIC,17, [Attack("Foxfire", 7), Attack("Illusion", 5)]),
        CreatureCard("Zombie",    Type.UNDEAD,18, [Attack("Undead Bite", 6), Attack("Grave Stench", 5)]),
        CreatureCard("Siren",     Type.WATER, 17, [Attack("Melodic Charm", 7), Attack("Drowning Song", 6)]),
        CreatureCard("Pegasus",   Type.AIR,   18, [Attack("Sky Strike", 7), Attack("Gale Wind", 6)]),
        CreatureCard("Gargoyle",  Type.EARTH, 20, [Attack("Stone Gaze", 6), Attack("Granite Slam", 7)]),
        CreatureCard("Archangel", Type.LIGHT, 21, [Attack("Divine Light", 8), Attack("Winged Fury", 7)]),
        CreatureCard("Goblin",    Type.EARTH, 14, [Attack("Sneak Attack", 5), Attack("Nimble Strike", 6)]),
        CreatureCard("Gollum",    Type.DARK,  15, [Attack("Cunning Ambush", 7), Attack("Twisted Pummel", 6)]),
    ]

def base_enhancements() -> List[EnhancementCard]:
    return [
        EnhancementCard(
            "Volcanic Terrain",
            "+3 damage to FIRE attacks you make.",
            modifiers={"attack_bonus_by_type": {Type.FIRE: 3}}
        ),
        EnhancementCard(
            "Mystic Forest",
            "Reduce damage your creatures take by 2.",
            modifiers={"flat_damage_reduction": 2}
        ),
        EnhancementCard(
            "Ancient Ruins",
            "+1 damage to ARCANE attacks you make.",
            modifiers={"attack_bonus_by_type": {Type.ARCANE: 1}}
        ),
    ]

def build_deck(rng: random.Random) -> List[object]:
    # Simple deck: 3x each creature, 2x each enhancement, shuffled
    deck: List[object] = []
    for c in base_creatures():
        deck.extend([CreatureCard(c.name, c.ctype, c.max_hp, c.attacks)] * 3)
    for e in base_enhancements():
        deck.extend([EnhancementCard(e.name, e.text, e.modifiers)] * 2)
    rng.shuffle(deck)
    return deck
