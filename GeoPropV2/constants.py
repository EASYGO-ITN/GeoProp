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

R_bar = 83.144598  # bar.cm3/(mol.K)
R = 8.3144598  # Pa m3/mol/K


