from .Phases import PhaseType
from .Databases import LookUp
from .ErrorHandling import Error
from .Fluid import Fluid

import reaktoro as rkt
from enum import Enum
from typing import List, Union, Dict, Tuple, NoReturn, Optional
import time


def initFromElements(fluid: Fluid, options) -> Tuple[rkt.GaseousPhase, rkt.AqueousPhase, rkt.MineralPhase, str]:
    """
        initialises the partition species from elements

        Parameters
        ----------
        fluid: Fluid
            the fluid to be partitioned
        options: ReaktoroPartitionOptions
            the partitioning options

        Returns
        -------
        gaseous: rkt.GaseousPhase
            rkt.GaseousPhase object containing all possible gaseous species
        aqueous: rkt.AqueousPhase
            rkt.AqueousPhase object containing all possible aqueous species
        mineral: rkt.MineralPhase
            rkt.MineralPhase object containing all possible mineral species
        elements: str
            string array of all elements used

        Raises
        ------
        Nothing

    """

    # create a string array of the elements (space separated)
    elements = ""
    for i in fluid.total.elements:
        elements += i + " "
    elements = elements[:-1]

    # create a gaseous phase of all possible species from the given elements
    gaseous = rkt.GaseousPhase(rkt.speciate(elements))

    # set the activity model if the phase has any species
    if gaseous.elements():
        gaseous.setActivityModel(options.gaseousActivityModel.value())

    # create an aqueous phase of all possible species from the given elements
    aqueous = rkt.AqueousPhase(rkt.speciate(elements), rkt.exclude("organics"))
    # aqueous = rkt.AqueousPhase(elements)

    # set the activity model if the phase has any species
    if aqueous.elements():
        aqueous.setActivityModel(options.aqueousActivityModel.value())

        # set a CO2 specific activity model
        if options.aqueousCO2ActivityModel.value is not None:
            if "C" in fluid.total.elements and "O" in fluid.total.elements:
                if options.aqueousActivityModel == options.AqueousActivityModels.IDEAL:
                # cannot use the Ideal model with the CO2 activity model? - check with Alan
                    aqueous.setActivityModel(rkt.chain(options.AqueousActivityModels.HKF.value(),
                                                       options.aqueousCO2ActivityModel.value(("CO2"))))
                else:
                    aqueous.setActivityModel(rkt.chain(options.aqueousActivityModel.value(),
                                                       options.aqueousCO2ActivityModel.value(("CO2"))))

    # create a mineral phase of all possible species from the given elements
    mineral = rkt.MineralPhases(rkt.speciate(elements))

    # set the activity model if the phase has any species
    if options.mineralActivityModel != ReaktoroPartitionOptions.MineralActivityModels.IDEAL:
        mineral.setActivityModel(options.mineralActivityModel.value())

    return gaseous, aqueous, mineral, elements


def initFromSpecies(fluid: Fluid, options) -> Tuple[rkt.GaseousPhase, rkt.AqueousPhase, rkt.MineralPhase, str]:
    """
        initialises the partition species from the specified species

        Parameters
        ----------
        fluid: Fluid
            the fluid to be partitioned
        options: ReaktoroPartitionOptions
            the partitioning options

        Returns
        -------
        gaseous: rkt.GaseousPhase
            rkt.GaseousPhase object containing all gaseous species
        aqueous: rkt.AqueousPhase
            rkt.AqueousPhase object containing all aqueous species
        mineral: rkt.MineralPhase
            rkt.MineralPhase object containing all mineral species
        elements: str
            string array of all elements used

        Raises
        ------
        Error
            if the aqueous phase is not charge balanced

    """

    # create a string array of the elements (space separated)
    elements = ""
    for i in fluid.total.elements:
        elements += i + " "
    elements = elements[:-1]

    # initialise the aqueous, gaseous and mineral phases
    aqueous = rkt.AqueousPhase()
    gaseous = rkt.GaseousPhase()
    mineral = rkt.MineralPhases()


    charge = 0
    aqueous_str = ""
    if fluid.aqueous.components:

        # check that the aqueous phase is charge balanced (all fluids should be charge balanced)
        for i in fluid.aqueous.components:
            aqueous_str += i.value.alias["RKT"] + " "
            charge += i.value.charge * fluid.total.moles[i]
        aqueous_str = aqueous_str[:-1]

        charge *= 1/sum([fluid.aqueous.moles[i] for i in fluid.aqueous.moles])

        # raise error if the specific charge difference exceeds a threshold
        if abs(charge) > 1e-3:
            raise Error("\n\nThe aqueous phase is not charge balanced. The excess charge is {:.4e}.\nPlease review the input data\n".format(charge))

        # populate the aqueous phase with species and apply the selected activity model
        aqueous = rkt.AqueousPhase(aqueous_str)
        aqueous.setActivityModel(options.aqueousActivityModel.value())

        # apply the CO2 activity model (if selected)
        if options.aqueousCO2ActivityModel.value is not None:
            if "CO2(aq)" in aqueous_str:
                aqueous.setActivityModel(rkt.chain(options.aqueousActivityModel.value(),
                                                   options.aqueousCO2ActivityModel.value("CO2")))

    gaseous_str = ""
    if fluid.gaseous.components:
        for i in fluid.gaseous.components:
            gaseous_str += i.value.alias["RKT"] + " "
        gaseous_str = gaseous_str[:-1]

        # populate the gaseous phase with species and apply the selected activity model
        gaseous = rkt.GaseousPhase(gaseous_str)
        gaseous.setActivityModel(options.gaseousActivityModel.value())

    mineral_str = ""
    if fluid.mineral.components:
        for i in fluid.mineral.components:
            mineral_str += i.value.alias["RKT"] + " "
        mineral_str = mineral_str[:-1]

        # populate the mineral phase with species and apply the selected activity model
        mineral = rkt.MineralPhases(mineral_str)
        # TODO need to fix the below
        # if options.mineralActivityModel == ReaktoroPartitionOptions.MineralActivityModels.IDEAL:
        #     mineral.setActivityModel(options.mineralActivityModel.value(rkt.StateOfMatter.Solid))
        # else:
        #     mineral.setActivityModel(options.mineralActivityModel.value())

    return gaseous, aqueous, mineral, elements


class ReaktoroPartitionOptions:
    """
        The ReaktoroPartitionOptions class contains all options seetings for a Reaktoro partition

        Attributes
        ----------
        database: self.Database
            the species database to be used
        speciesMode: self.SpeciesMode
            the method for generating the partitioning species
        aqueousActivityModel: self.AqueousActivityModel
            the activity model to be used for the aqueous phase
        aqueousCO2ActivityModel: self.AqueousCO2ActivityModel
            the activity model to be used for aqueous CO2
        gaseousActivityModel: self.GaseousActivityModels
            the activity model to be used for the gaseous phase
        mineralActivityModel: self.MineralActivityModels
            the activity model to be used for the mineral phase
        strictSucess: bool
            flag to decided whether only fully converged results are to be accepted
        debug: bool
            flag to decide whether to output a debug of the reaktoro partitioning
        debugFileName: str
            the file location of where the reaktoro debug file will be written

        Raises
        ------
        Nothing
    """

    class Database(Enum):
        """
            the Database class contains the reaktoro databases that can be used for the partition
        """
        SUPCRTBL = "supcrtbl"

    class SpeciesMode(Enum):
        """
            the SpeciesMode class contains links to the methods for generating the partitioning species
        """
        ALL = initFromElements
        SELECTED = initFromSpecies

    class AqueousActivityModels(Enum):
        """
            The AqueousActivityModels class contains links to all the activity model that can be used for the aqueous phase
        """
        IDEAL = rkt.ActivityModelIdealAqueous
        DAVIES = rkt.ActivityModelDavies
        DEBYE_HUCKEL = rkt.ActivityModelDebyeHuckel
        DEBYE_HUCKEL_KIELLAND = rkt.ActivityModelDebyeHuckelKielland
        DEBYE_HUCKEL_LIMITINGLAW = rkt.ActivityModelDebyeHuckelLimitingLaw
        DEBYE_HUCKEL_PARAMS = rkt.ActivityModelDebyeHuckelParams
        DEBYE_HUCKEL_PHREEQC = rkt.ActivityModelDebyeHuckelPHREEQC
        DEBYE_HUCKEL_WATEQ4F = rkt.ActivityModelDebyeHuckelWATEQ4F
        HKF = rkt.ActivityModelHKF
        PITZER_HMW = rkt.ActivityModelPitzerHMW

    class AqueousCO2ActivityModels(Enum):
        """
            The AqueousCO2ActivityModels class contains links to all the activity model that can be used for aqueous CO2
        """
        NONE = None
        DRUMMOND = rkt.ActivityModelDrummond
        DUAN_SUN = rkt.ActivityModelDuanSun
        RUMPF = rkt.ActivityModelRumpf

    class GaseousActivityModels(Enum):
        """
            The GaseousActivityModels class contains links to all the activity model that can be used for the gaseous phase
        """
        IDEAL = rkt.ActivityModelIdealGas
        PENG_ROBINSON = rkt.ActivityModelPengRobinson
        REDLICH_KWONG = rkt.ActivityModelRedlichKwong
        SOAVE_REDLICH_KWONG = rkt.ActivityModelSoaveRedlichKwong
        VAN_DER_WAALS = rkt.ActivityModelVanDerWaals

    class MineralActivityModels(Enum):
        """
            The MineralActivityModels class contains links to all the activity model that can be used for the mineral phase
        """
        IDEAL = rkt.ActivityModelIdealAqueous()
        REDLICH_KISTER = rkt.ActivityModelRedlichKister

    def __init__(self):
        """
            initialises the ReaktoroPartitionOptions
        """

        self.database = self.Database.SUPCRTBL
        self.speciesMode = self.SpeciesMode.ALL

        self.aqueousActivityModel = self.AqueousActivityModels.IDEAL
        self.aqueousCO2ActivityModel = self.AqueousCO2ActivityModels.NONE
        self.gaseousActivityModel = self.GaseousActivityModels.IDEAL
        self.mineralActivityModel = self.MineralActivityModels.IDEAL

        self.strictSucess = True  # raise an error if solve does not converge

        self.debug = False  # create file of reaktoro results
        self.debugFileName = "ReaktoroResults.txt"


class ReaktoroPartition:
    """
        The ReaktoroPartition class orchestrates the fluid partition using Reaktoro

        TODO a P-H Equilibration would be cool too...
    """

    @staticmethod
    def calc(fluid: Fluid, P: float, T: float, options: ReaktoroPartitionOptions) -> Fluid:
        """
            calculates the fluid partition using Reaktoro

            Parameters
            ----------
            fluid: Fluid
                the fluid to be partitioned
            P: float
                the pressure in Pa
            T: float
                the temperature in K
            options: ReaktoroPartitionOptions
                the options to be used for the partition calculations

            Returns
            -------
            Fluid

            Raises
            ------
            Assertion
                if the equilibration is not successful (provided this check has not been disabled)
        """

        # initialise the reaktoro database to be used
        db = rkt.SupcrtDatabase(options.database.value)

        # generates the aqueous, gaseous and mineral phases
        aqueous, gaseous, mineral, elements = options.speciesMode(fluid, options)

        # creates the chemical system
        try:
            system = rkt.ChemicalSystem(db, aqueous, gaseous, mineral)
        except:
            # TODO - this is a bit of a hack and obviously only works if there is only mineral phase missing
            system = rkt.ChemicalSystem(db, aqueous, gaseous)

        # initialise a material class
        mix = rkt.Material(system)

        # set the composition of each species
        for i in range(len(fluid.total.components)):
            comp = fluid.total.components[i]
            mix.add(comp.value.alias["RKT"], fluid.total.mass[comp], "kg")

        # add a little bit of some commonly troublesome species (not very clean but it works)
        if options.speciesMode == ReaktoroPartitionOptions.SpeciesMode.ALL:
            # this is a total fudge....
            if "O" in elements:
                mix.add("O2(aq)", 1e-15, "kg")
            if "H" in elements:
                mix.add("H2(aq)", 1e-15, "kg")

        # equilibrate the fluid
        state = mix.equilibrate(T, "K", P, "Pa")
        res = mix.result()

        # check if the equilibration converged
        if options.strictSucess:
            assert res.optima.succeeded

        # print a debug file for the equilibration
        if options.debug:
            state.output(options.debugFileName)

        # get the resultant components and component masses from all phases
        species = {}
        masses = {}
        for phase in state.system().phases().data():

            # determine the phase type
            if phase.name() == "AqueousPhase":
                key = PhaseType.AQUEOUS
            elif phase.name() == "GaseousPhase":
                key = PhaseType.GASEOUS
            elif phase.name() == "MineralPhase":
                key = PhaseType.MINERAL
            elif phase.aggregateState().name == "Solid":
                key = PhaseType.MINERAL
            else:
                raise Error("\n\n Invalid phase encountered")

            # this was not quite working because each mineral species is treated as a separate phase, so it was just
            # overwriting the mineral components
            # # get the Comp object and mass for each species in a phase
            # species[key] = [LookUp().withReaktoroName(i.name()) for i in phase.species().data()]
            # masses[key] = [state.speciesMass(i.name())[0] for i in phase.species().data()]

            if key not in species:
                species[key] = [LookUp().withReaktoroName(i.name()) for i in phase.species().data()]
                masses[key] = [state.speciesMass(i.name())[0] for i in phase.species().data()]
            else:
                species[key] += [LookUp().withReaktoroName(i.name()) for i in phase.species().data()]
                masses[key] += [state.speciesMass(i.name())[0] for i in phase.species().data()]

        # populate the components and composition array for fluid creation
        components = []
        composition = []
        for i in species:
            for j in range(len(species[i])):
                components.append(species[i][j])
                composition.append(masses[i][j])

        # create a new fluid
        return Fluid(components=components, composition=composition)