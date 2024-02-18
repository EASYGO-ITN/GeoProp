from enum import Enum
from typing import List, Union, Dict, Tuple, NoReturn, Optional


class PhaseType(Enum):
    """
        The PhaseType class summarises all the possible phases
    """
    LIQUID = "liquid"
    AQUEOUS = "aqueous"
    GASEOUS = "gaseous"
    MINERAL = "mineral"
    TOTAL = "total"
    ELEMENT = "element"
    NONE = "none"


class PhaseProperties:
    """
        The PhaseProperties class summarises the properties of a given phase

        Attributes
        ----------
        P: int, float
            the phase pressure in MPa
        T: int, float
            the phase temperature in K
        h: int, float
            the phase specific enthalpy in kJ/kg
        s: int, float
            the phase specific entropy in kJ/kg/K
        rho: int, float
            the phase density in kg/m3
        v: int, float
            the phase specific volume in m3/kg
        m: int, float
            the total mass of this phase
        NotCalculated: list
            list of components that could not be calculated

    """

    def __init__(self, props):
        """
            Initialises the PhaseProperties object

            Parameters
            ----------
            props: Dict
                dictionary of the fluid properties

        """
        props0 = {"P": 0, "T": 0, "h": 0, "s": 0, "rho": 0, "v": 0, "m": 0, "NotCalculated": []}

        for i in props:
            props0[i] = props[i]

        # creates a variable for each of the items in props
        vars = (i for i in props0)  # plus plenty more

        # assigns the value to each property
        for i in vars:
            setattr(self, i, props0[i])

    def __getitem__(self, item: str):
        """
            Allows the property to be retrieved by either "PhaseProperties.xzy" or "PhaseProperties["xyz"]

            Parameters
            ----------
            item: str
                the name of the property to return. Valid properties as p, t, h, s, x, rho, phase, fluid for now

            Returns
            -------
            float, int
        """

        item = "" + item
        return getattr(self, item)

    def __str__(self):
        """
            Determines the string representation of PhaseProperties objects

            Returns
            -------
            text : str
                text string that encompasses all relevant information about the Fluid object
        """

        text = "P: {:.4e} Pa\tT: {} K\th: {:.4e} kJ/kg\t\ts: {:.4e} kJ/kg/K\trho: {:.4e} kg/m3\tv: {:.4} m3/kg\tm: {:.4e} kg".format(self.P, self.T, self.h, self.s, self.rho, self.v, self.m)
        if self.NotCalculated:
            text += "\nThe following components were not calculated: {}".format(self.NotCalculated)

        return text

    def copy(self):

        newProps = {"P": 0.0, "T": 0.0, "h": 0.0, "s": 0.0, "rho": 0.0, "m": 0.0, "v":0.0}
        newProps = {i: self[i]*1.0 for i in newProps}

        if self.NotCalculated:
            newProps["NotCalculated"] = [i for i in self.NotCalculated]
        else:
            newProps["NotCalculated"] = None

        return PhaseProperties(newProps)

class Phase:
    """
        The Phase class summarises components, compositions and properties of a phase

        Attributes
        ----------
        phase: PhaseType
            the type of the phase
        components: List[Comp]
            the components of the phase
        elements: Set
            the elements of the phase
        mass: Dict
            the mass of each component in kg
        moles: Dict
            the moles of each component in mol
        massfrac: List
            the mass fraction of each component
        molefrac: List
            the mole fraction of each component
        up_to_date: bool
            flag indicating whether the mass and mole fractions are up to date
        props: PhaseProperties
            the thermophysical properties of the phase
        props_calculated: bool
            flag indicating whether the physical properties have been calculated

    """

    def __init__(self):
        """
            Initialises the Phase object

        """
        self.phase = PhaseType.NONE
        self.components = []
        self.elements = {}

        self.mass = {}
        self.moles = {}

        self.massfrac = []
        self.molefrac = []
        self.up_to_date = True

        self.props = PhaseProperties({"P": 0.0, "T": 0.0, "h": 0.0, "s": 0.0, "rho": 0.0, "m": 0.0})
        self.props_calculated = False

    def __str__(self):
        """
           Creates the Phase object string representation

        """
        # print the phase type
        text = "Phase: {}\n\n".format(self.phase)

        # print the components in this phase
        text += "Components:\n"
        for comp in self.components:
            text += "{}, ".format(comp.name)
        text = text[:-2] + "\n\n"

        # print a table of components and their composition in this phase
        text += "Composition: \n{:20}|{:<15}|{:<15}|{:<15}|{:<15}|\n".format("Component", "Mass, kg", "MassFrac, -", "Moles, mol", "MoleFrac, -")
        text += "--------------------+---------------+---------------+---------------+---------------+\n"
        for i, comp in enumerate(self.components):
            text += "{:20}|{:15.3e}|{:15.3e}|{:15.3e}|{:15.3e}|\n".format(comp.name, self.mass[comp], self.massfrac[i], self.moles[comp], self.molefrac[i])

        # print the phase properties
        text += "\nProperties: " + str(self.props) + "\n"

        return text

    def add_component(self, comp, mass: float, moles: float, update: Optional[bool] =True) -> NoReturn:
        """
            Adds a component to the phase

            Parameters
            ----------
            comp: Comp
                The component to be added to the phase
            mass: float
                The mass of the component to be added
            moles: float
                The moles of the component to be added
            update: Optional[bool]
                Flag to determine whether the mass and mole fractions should be recalculated

            Returns
            -------
            NoReturn
        """

        # checks if component already exists in the phase
        if comp in self.components:
            # add the mass and moles to
            self.mass[comp] += mass
            self.moles[comp] += moles
        else:
            self.components.append(comp)
            self.mass[comp] = mass
            self.moles[comp] = moles

            # update the list of elements
            if len(self.elements) > 0:
                self.elements.update(comp.value.elements)
            else:
                self.elements = {i for i in comp.value.elements}

        # resets the flag for the mass and mole fractions being up to date
        self.up_to_date = False

        # if yes, recalculates the mass and mole fractions
        if update:
            self.update()

    def update(self) -> NoReturn:
        """
            Recalculates the mass and mole fractions of all components in the phase

            Returns
            -------
            NoReturn
        """

        # checks if the mass and mole fractions are already up to date
        if self.up_to_date:
            return

        # calculates the total mass and number of moles
        total_mass = sum(self.mass.values())
        total_moles = sum(self.moles.values())

        # calculates the mass and mole fractions of each species
        self.massfrac = [self.mass[self.components[i]] / (total_mass + 1e-15) for i in range(len(self.components))]
        self.molefrac = [self.moles[self.components[i]] / (total_moles +1e-15) for i in range(len(self.components))]

        # resets the phase properties
        self.props_calculated = False
        self.props = PhaseProperties({"P": 0.0,  "T": 0.0, "h": 0.0, "s": 0.0, "rho": 0.0, "v": 0.0, "m": 0.0, "NotCalculated": []})

        # sets the flag that the mass and mole fractions are up to date
        self.up_to_date = True


class LiquidPhase(Phase):
    """
        The LiquidPhase class summarises components, compositions and properties of a liquid phase
    """

    def __init__(self):
        super().__init__()

        # set the phase type
        self.phase = PhaseType.LIQUID


class AqueousPhase(Phase):
    """
        The AqueousPhase class summarises components, compositions and properties of an aqueous phase
    """

    def __init__(self):
        super().__init__()

        # set the phase type
        self.phase = PhaseType.AQUEOUS


class GaseousPhase(Phase):
    """
        The GaseousPhase class summarises components, compositions and properties of a gaseous phase
    """

    def __init__(self):
        super().__init__()

        # set the phase type
        self.phase = PhaseType.GASEOUS


class MineralPhase(Phase):
    """
        The MineralPhase class summarises components, compositions and properties of a mineral phase
    """

    def __init__(self):
        super().__init__()

        # set the phase type
        self.phase = PhaseType.MINERAL


class ElementPhase(Phase):
    """
        The MineralPhase class summarises components, compositions and properties of a mineral phase
    """

    def __init__(self):
        super().__init__()

        # set the phase type
        self.phase = PhaseType.ELEMENT


class TotalPhase(Phase):
    """
        The TotalPhase class summarises components, compositions and properties of all phases

        Attributes
        ----------
        phases: List[Phases]

    """

    def __init__(self):
        super().__init__()

        # set the phase type
        self.phase = PhaseType.TOTAL
        self.phases = {}

