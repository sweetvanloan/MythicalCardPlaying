from enum import Enum, auto

class Type(Enum):
    FIRE = auto()
    WATER = auto()
    EARTH = auto()
    LIGHT = auto()
    DARK = auto()
    ARCANE = auto()
    AIR = auto()
    SPIRIT = auto()
    MYSTIC = auto()
    SEA = auto()
    UNDEAD = auto()

class Phase(Enum):
    DRAW = auto()
    MAIN = auto()
    ATTACK = auto()
    END = auto()
