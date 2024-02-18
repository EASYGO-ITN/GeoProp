from .Phases import *
from .Databases import Comp
from .ErrorHandling import Error, InputError

import copy
from typing import List, Union, NoReturn, Optional
import numpy as np


class Fluid:
    """
    The Fluid class combines all phases (aqueous, gaseous and mineral)

    Attributes
    ----------
    total : Phase
    aqueous : Phase
    liquid : Phase
    gaseous : Phase
    mineral : Phase

    # TODO something to scale the fluid (i.e. based on mass or volume)

    """
    def __init__(self, components: Optional[Union[List[Comp], Comp]] = None, composition: Optional[Union[List[float], float]] = None, CompInMole: Optional[bool]=False):
        """
        Initialises a Fluid object from components and composition (optional)

        Parameters
        ----------
        components (opt): Union[List[Comp], Comp]
            the component(s) to be added to the fluid
        composition (opt): Union[List[Union[int, float]], Union[int, float]
            the composition of the component(s) to be added to the fluid in kg
        CompInMole (opt): bool

        Returns
        -------
        Fluid
            a Fluid object

        """

        # initialise the phases
        self.total = TotalPhase()
        self.aqueous = AqueousPhase()
        self.liquid = LiquidPhase()
        self.gaseous = GaseousPhase()
        self.mineral = MineralPhase()
        self.element = ElementPhase()

        # add the components to the fluid
        if components is not None and composition is not None:
            self.addComponents(components, composition, CompInMole)

    def addComponent(self, component: Comp, composition: float, CompInMole: bool,update: Optional[bool] =True) -> NoReturn:
        """
        add a component to the Fluid

        Parameters
        ----------
        component : Comp
            the component to be added to the FLuid
        composition : Union[int, float]
            the mass of the component to be added to the Fluid in kg
        CompInMole: bool
            flag to indicate if the composition is in mass or mole
        update : bool
            flag to trigger the recalculation of mass and mole fractions


        Returns
        -------
        NoReturn

        Raises
        ------
        InputError
            if the component does not exist in the database
            if the composition is not in the correct format
        Error
            if the component's native phase is not recognised

        """

        # check that all components exist within the database
        if type(component) != Comp:
            message = "\n\nThe component '{}' does not exist in the database\n".format(component)
            raise InputError(message)

        # check that the composition is a number
        if type(composition) not in [int, float, np.float64]:
            message = "\n\nThe composition of component '{}' is incorrectly formatted (int or float expected)\n".format(component)
            raise InputError(message)

        # determine the inputs
        comp = component


        if not CompInMole:
            mass = composition
            moles = mass / comp.value.Mr
        else:
            moles = composition
            mass = moles * comp.value.Mr
        phase = comp.value.phase

        # add the component to the respective phase
        self.total.add_component(comp, mass, moles, update=update)

        # add component to the aqueous phase
        if phase == PhaseType.AQUEOUS:
            self.aqueous.add_component(comp, mass, moles, update=update)
            self.total.phases[PhaseType.AQUEOUS] = self.aqueous

            return

        # add component to the liquid phase
        if phase == PhaseType.LIQUID:
            self.liquid.add_component(comp, mass, moles, update=update)
            self.total.phases[PhaseType.LIQUID] = self.liquid

            return
        # add component to the gaseous phase
        if phase == PhaseType.GASEOUS:
            self.gaseous.add_component(comp, mass, moles, update=update)
            self.total.phases[PhaseType.GASEOUS] = self.gaseous

            return

        # add component to the mineral phase
        if phase == PhaseType.MINERAL:
            self.mineral.add_component(comp, mass, moles, update=update)
            self.total.phases[PhaseType.MINERAL] = self.mineral

            return

        # add component to the element phase
        if phase == PhaseType.ELEMENT:
            self.element.add_component(comp, mass, moles, update=update)
            self.total.phases[PhaseType.ELEMENT] = self.element

            return

        raise Error("\n\nThe component's native phase is not recognised. Component:{}".format(component))

    def addComponents(self, components: List[Comp], composition: List[float], CompInMole: bool) -> NoReturn:
        """
        add components to the Fluid

        Parameters
        ----------
        components : Comp
            the component to be added to the FLuid
        composition : Union[int, float]
            the mass of the component to be added to the Fluid in kg
        CompInMole: bool
            flag to indicate if the composition is in mass or mole

        Returns
        -------
        NoReturn

        Raises
        ------
        InputError
            if the number of components and composition is inconsistent

        """

        # check that equal numbers of components and composition have been defined
        if len(components) != len(composition):
            raise InputError("\n\nThe number of components and compositions provided is not the same")

        # add each component to the fluid
        for i in range(len(components)):
            self.addComponent(components[i], composition[i], CompInMole, update=False)

        # re-calculate the component mass and mole fractions
        self.total.update()
        self.liquid.update()
        self.aqueous.update()
        self.gaseous.update()
        self.mineral.update()

    def promotePhaseToFluid(self, phaseType: PhaseType):
        """
        create a Fluid object for a given Phase

        Parameters
        ----------
        phaseType : PhaseType
            the phase from which the FLuid should be created

        Returns
        -------
        Fluid
            the new Fluid object

        """

        # check if the phase is the total phase
        if phaseType == PhaseType.TOTAL:
            phase = self.total
        else:
            phase = self.total.phases[phaseType]

        components = [i for i in phase.components]
        composition = [phase.mass[i] * 1.0 for i in components]
        props = phase.props.copy()

        # create the new fluid from the components and composition
        newFluid = Fluid(components=components, composition=composition)

        # set the total and phase properties
        newFluid.total.props = props
        if self.total.props_calculated:
            newFluid.total.props_calculated = True
        else:
            newFluid.total.props_calculated = False

        if phaseType != PhaseType.TOTAL:
            newFluid.total.phases[phaseType].props = props

        return newFluid

    def promotePhasesToFluid(self, phaseTypes: List[PhaseType]):
        """
        create a Fluid object from given Phases

        Parameters
        ----------
        phaseTypes : List[PhaseType]
            the phases from which the FLuid should be created

        Returns
        -------
        Fluid
            the new Fluid object

        """

        # check if the total phase is one of the phases to be copied
        if PhaseType.TOTAL in phaseTypes:
            return copy.deepcopy(self)  # just return a deepcopy of the fluid

        # create the component and composition lists to generate the new fluid
        phases = {}
        components = []
        composition = []
        for phaseType in phaseTypes:
            phase = self.total.phases[phaseType]  # retrieve the current phase
            phases[phaseType] = phase  # store the current phase - this will be needed for the properties later
            components = components + [i for i in phase.components]
            composition = composition + [phase.mass[i] for i in phase.components]

        # create the new fluid from the components and composition
        newFluid = Fluid(components=components, composition=composition)

        for phaseType in phaseTypes:
            # set the phase properties
            newFluid.total.phases[phaseType].props = phases[phaseType].props.copy()

        newFluid._totalPhaseProps()

        return newFluid

    def copy(self):
        phases = self.total.phases
        return self.promotePhasesToFluid(phases)

    def _totalPhaseProps(self):
        # init the total enthalpy, entropy, volume, mass and any components that could not be calculated
        enthalpy = 0
        entropy = 0
        volume = 0.
        mass = 0
        comp_not_calculated = []

        for phase in self.total.phases:
            phase = self.total.phases[phase]
            enthalpy += phase.props["h"] * phase.props["m"]
            entropy += phase.props["s"] * phase.props["m"]

            if phase.props["rho"] != 0:
                volume += phase.props["m"] / (phase.props["rho"] + 1e-6)

            mass += phase.props["m"]

            P = phase.props["P"] * 1.0
            T = phase.props["T"] * 1.0

            if phase.props["NotCalculated"]:
                comp_not_calculated = comp_not_calculated + phase.props["NotCalculated"]

        # calculate the total mass
        total_mass = sum([self.total.mass[i] for i in self.total.mass])

        # check if the total mass from the composition is consistent with the mass of the components in phases
        if (total_mass - mass) / total_mass > 1e-3:
            raise Error(
                "The calculation has lost mass. Current loss: {} %".format(100 * (total_mass - mass) / total_mass))

        # calculate the specific properties
        props = {"P": P,
                 "T": T,
                 "h": enthalpy / total_mass,
                 "s": entropy / total_mass,
                 "rho": total_mass / (volume + 1e-6),
                 "v": volume / total_mass,
                 "m": total_mass,
                 "NotCalculated": comp_not_calculated}

        self.total.props = PhaseProperties(props)
        self.total.props_calculated = True

    def __str__(self) -> str:
        """
        creates the Fluid's string representation, i.e. to allow it to be printed

        Returns
        -------
        str
            the Fluid object's string representation

        """
        # print the phase name
        total = self.total
        text = "Phase: {}\n\n".format(total.phase.name)

        # print the names of all components in said phase
        text += "Components:\n"
        for comp in total.components:
            text += "{}, ".format(comp.name)
        text = text[:-2] + "\n\n"

        # print a table of all components and their composition provided they make up more than 1e-10 mol
        text += "Composition: \n{:20}|{:<15}|{:<15}|{:<15}|{:<15}|{:<15}|\n".format("Component", "Mass, kg", "MassFrac, -", "Moles, mol", "MoleFrac, -", "In Phase")
        text += "--------------------+---------------+---------------+---------------+---------------+---------------+\n"
        for i, comp in enumerate(total.components):
            if total.moles[comp] > 1e-10:
                text += "{:20}|{:15.3e}|{:15.3e}|{:15.3e}|{:15.3e}|{:>15}|\n".format(comp.name, total.mass[comp], total.massfrac[i], total.moles[comp], total.molefrac[i], comp.value.phase.name)
        text += "--------------------+---------------+---------------+---------------+---------------+---------------+\n"

        # print a table of all phase properties, provided the phase exists
        text += "\n"
        if self.total.props_calculated:
            text += "Properties: \n"
            text += "Pressure: {} Pa\n".format(self.total.props["P"])
            text += "Temperature: {} K\n".format(self.total.props["T"])
            text += "{:20}|{:<15}|{:<18}|{:<15}|{:<15}|{:<15}|\n".format("Phase", "Enthalpy, kJ/kg", "Entropy, kJ/kg/K", "Rho, kg/m3", "Volume, m3/kg", "Mass, kg")
            text += "--------------------+-----------------+----------------+---------------+---------------+---------------+\n"
            if self.aqueous.components:
                text += "{:20}|{:15.3e}|{:18.3e}|{:15.3e}|{:15.3e}|{:15.3e}|\n".format(self.aqueous.phase.name, self.aqueous.props["h"], self.aqueous.props["s"], self.aqueous.props["rho"], self.aqueous.props["v"], self.aqueous.props["m"])
            if self.gaseous.components:
                text += "{:20}|{:15.3e}|{:18.3e}|{:15.3e}|{:15.3e}|{:15.3e}|\n".format(self.gaseous.phase.name, self.gaseous.props["h"], self.gaseous.props["s"], self.gaseous.props["rho"], self.gaseous.props["v"], self.gaseous.props["m"])
            if self.mineral.components:
                text += "{:20}|{:15.3e}|{:18.3e}|{:15.3e}|{:15.3e}|{:15.3e}|\n".format(self.mineral.phase.name, self.mineral.props["h"], self.mineral.props["s"], self.mineral.props["rho"], self.mineral.props["v"], self.mineral.props["m"])
            text += "--------------------+-----------------+----------------+---------------+---------------+---------------+\n"
            text += "{:20}|{:15.3e}|{:18.3e}|{:15.3e}|{:15.3e}|{:15.3e}|\n".format(self.total.phase.name, self.total.props["h"], self.total.props["s"], self.total.props["rho"], self.total.props["v"], self.total.props["m"])
            text += "--------------------+-----------------+----------------+---------------+---------------+---------------+\n"

            # print components that could not be calculated
            if self.total.props.NotCalculated:
                txt = ""
                mass = 0
                for i in self.total.props.NotCalculated:
                    txt += i.value.name + ", "
                    mass += self.total.mass[i]
                txt = txt[:-2]

                text += "The following had to be excluded: {}\n".format(txt)
                text += "This corresponds to a mass of {:.4e} kg or {:.4e} % of the total".format(mass, 100*mass/self.total.props["m"])

        else:
            text += "Properties not yet calculated"
        return text

    def cullComponents(self, moleLimit: Optional[float] = 1e-15, in_place: Optional[bool] = True):
        """
            allows components below a certain mole fraction to be removed from the fluid - useful for speeding up property calculations

            Parameters
            ----------
            moleLimit: Optional[float]
                the cut-off below which components will be excluded from the calculations
            in_place: Optional[bool]
                whether the fluid itself is overwritten or a new fluid is created.

            Returns
            -------
            Fluid: Fluid
        """
        # get all components and their composition that are above the mole cut-off
        components = [comp for comp in self.total.components if self.total.moles[comp] > moleLimit]
        composition = [self.total.mass[comp] for comp in components]

        if in_place:
            # make changes to the fluid itself
            self.reset()

            self.addComponents(components, composition, False)
            return self
        else:
            # create a new fluid object
            return Fluid(components=components, composition=composition)

    def cullPhase(self, phaseType: PhaseType, in_place: Optional[bool] = True):
        """
            removes the specified phase from the fluid

            Parameters
            ----------
            phaseType: PhaseType
                the phase to be removed
            in_place: bool
                whether the fluid itself is overwritten or a new fluid is created

            Returns:
            Fluid: Fluid
        """
        # get all components and their composition not in the specified phase
        components = [comp for comp in self.total.components if comp.value.phase != phaseType]
        composition = [self.total.mass[comp] for comp in components]

        if in_place:
            # updates the fluid itself
            self.reset()
            self.addComponents(components, composition, False)

            return self
        else:
            # creates a new Fluid
            return Fluid(components=components, composition=composition)

    def reset(self) -> NoReturn:
        """
            reinitialises the Fluid object

            Returns
            -------
            NoRetrur

            Raises
            ------
            Nothing
        """

        self.total = TotalPhase()
        self.aqueous = AqueousPhase()
        self.liquid = LiquidPhase()
        self.gaseous = GaseousPhase()
        self.mineral = MineralPhase()
        self.element = ElementPhase()

    def normaliseComposition(self):

        components = [i for i in self.total.components]
        mass_corr = 1 / sum([self.total.mass[i] for i in components])

        self.total.mass = {i:self.total.mass[i]*mass_corr for i in components}
        self.total.moles = {i:self.total.moles[i]*mass_corr for i in components}

        if self.total.props_calculated:
            self.total.props.m *= mass_corr

        for phaseType in self.total.phases:
            phase = self.total.phases[phaseType]
            phase.mass = {i:phase.mass[i] * mass_corr for i in phase.components}
            phase.moles = {i:phase.moles[i] * mass_corr for i in phase.components}

            if self.total.props_calculated:
                phase.props.m *= mass_corr