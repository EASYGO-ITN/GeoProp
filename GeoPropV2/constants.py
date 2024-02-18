from enum import Enum


class PhaseType(Enum):

    LIQUID = "liquid"
    AQUEOUS = "aqueous"
    VAPOUR = "vapour"
    SOLID = "solid"
    TOTAL = "total"
    ELEMENT = "element"
    NONE = "none"

class Units(Enum):
    MOL = "mol"
    MASS = "mass"

