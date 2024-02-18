from .Databases import Comp
from .Phases import Phase
from .Constants import *

from enum import Enum
import os
import thermohubclient
import thermofun as fun
import CoolProp as cp
from typing import List, Union, Dict, Tuple, NoReturn, Optional


class ThermoFunPropertyOptions:
    """
        The ThermoFunPropertyOptions class contains all of the ThermoFun property calculation options

        Classes
        -------
        Database

        Attributes
        ----------
        database: self.Database
            the ThermoFun database to be used
        databaseHomeDir: str
            the home director of the ThermoFun database - relative to the project's home directory
        databaseConfigFile: str
            the name of the ThermoHub configuration file - in the databaseHomeDir directory
        massfracCutOff: float
            the minimum mass fraction for a species to be included in the property calculations

    """

    class Database(Enum):
        """
            Database sub-class contains all the ThermoFun databases that can be used
        """
        AQ17 = "aq17-thermofun.json"
        CEMDATA18 = "cemdata18-thermofun.json"
        HERACLES = "heracles-thermofun.json"
        MINES16 = "mines16-thermofun.json"
        MINES19 = "mines19-thermofun.json"
        PSINAGRA = "psinagra-12-07-thermofun.json"
        SLOP16 = "slop16-thermofun.json"
        SLOP98INORGANIC = "slop98-inorganic-thermofun.json"
        SLOP98ORGANIC = "slop98-organic-thermofun.json"
        SLOP98INORGANIC_CUT = "slop98-inorganic-thermofun_cut.json"

    def get_database(self, database: str):
        """
            retrieves the database from ThermoHub

            Parameters
            ----------
            database: str
                the ThermoFun database name
        """
        # get the home directory
        home = os.getcwd()

        # navigate to the ThermoFun directory
        ThermoFun_dir = home + "/" + self.databaseHomeDir
        os.chdir(ThermoFun_dir)

        # save the ThermoFun database
        dbc = thermohubclient.DatabaseClient(self.databaseConfigFile)
        dbc.saveDatabase(database.value)

        # navigate back to the home directory
        os.chdir(home)

    def __init__(self):
        """
            initialises the ThermoFunPropertyModelOptions
        """
        # self.database = self.Database.SLOP98INORGANIC_CUT
        self.database = self.Database.SLOP98INORGANIC
        self.databaseHomeDir = os.path.dirname(__file__).rstrip("\\Model")+"\\ThermoFun"
        self.databaseConfigFile = "hub-connection-config.json"

        self.engine = None

        self.massfracCutOff = 1e-6

    def init_engine(self):
        # initialise the ThermoFun database
        database = self.databaseHomeDir + "\\" + self.database.value

        # initialise the ThermoFun calculation engineer
        self.engine = fun.ThermoEngine(database)



class ThermoFunProperties:
    """
        The ThermoFunProperties class orchestrates the property calculations using ThermoFun
    """

    @staticmethod
    def calc(phase: Phase, P: float, T: float, options: ThermoFunPropertyOptions) -> Dict:
        """
            calculates the thermophysical properties of the phase at the specified temperature and pressure

            Parameters
            ----------
            phase: Phase
                the phase to be evaluated
            P: float
                the pressure in Pa
            T: float
                the temperature in K
            options: ThermoFunPropertyOptions
                the calculation options to be used

            Returns
            -------
            props: Dict

            Raises:
            Nothing
        """

        engine = None

        # initialise the property calculation results
        props = {"P": 0, "T": 0, "h": 0, "s": 0, "rho": 0, "v": 0, "m": 0, "NotCalculated": []}

        # initialise the phase total properties
        enthalpy = 0
        entropy = 0
        volume = 0
        comp_not_calculated = []

        for i, comp in enumerate(phase.components):

            if comp == Comp.WATER:
                # calculate the properties of water using CoolProp
                calc = cp.AbstractState("?", comp.value.alias["CP"])
                calc.specify_phase(cp.iphase_liquid)

                # calculate the enthalpy and entropy at the reference conditions
                calc.update(cp.PT_INPUTS, Pref, Tref)
                h0 = calc.hmass()
                s0 = calc.smass()

                calc.update(cp.PQ_INPUTS, P, 0)
                Tsat = calc.T()
                if T < Tsat:
                    # calculate the properties at the temperature and pressure of interest
                    calc.update(cp.PT_INPUTS, P, T)
                    h = calc.hmass()
                    s = calc.smass()
                    rho = calc.rhomass()
                else:
                    hsat = calc.hmass()
                    ssat = calc.smass()
                    rhosat = calc.rhomass()

                    calc.update(cp.PT_INPUTS, P, Tsat - 1)
                    dh = hsat - calc.hmass()
                    ds = ssat - calc.smass()
                    drho = rhosat - calc.rhomass()
                    dT = T - Tsat

                    h = hsat + dh * dT
                    s = ssat + ds * dT
                    rho = rhosat + drho * dT

                enthalpy += phase.mass[comp] * (h - h0) / 1e3
                entropy += phase.mass[comp] * (s - s0) / 1e3
                volume += phase.mass[comp] / rho

            elif phase.massfrac[i] > options.massfracCutOff:

                if engine is None:

                    if options.engine is None:
                        options.init_engine()

                    engine = options.engine

                # TODO it seems that the mass cut off results in mis reporting of phases when they are actually not there...

               # calculate the properties of the aqueous species
                try:

                    th_name = comp.value.alias["RKT"]
                    if "(aq)" in th_name:
                        th_name = th_name.replace("(aq)", "@")

                    properties = engine.thermoPropertiesSubstance(T, P, th_name)
                    properties0 = engine.thermoPropertiesSubstance(Tref, Pref, th_name)

                    enthalpy += phase.moles[comp] * (properties.enthalpy.val - properties0.enthalpy.val) / 1e3  # the units of enthalpy are J/mol
                    entropy += phase.moles[comp] * (properties.entropy.val - properties0.entropy.val) / 1e3  # the units of entropy are J/mol
                    volume += properties.volume.val * 1e-5 * phase.moles[comp]  # the units of volume are in J/bar
                    # It seems the species volume contribution can be negative... I guess this due to charge effects of the ions??

                except:
                    comp_not_calculated.append(comp)

        # calculate the total mass of the phase
        total_mass = sum([phase.mass[i] for i in phase.mass])

        # update the phase properties
        props["P"] = P
        props["T"] = T
        props["h"] = enthalpy / (total_mass + 1e-6)
        props["s"] = entropy / (total_mass + 1e-6)
        props["v"] = volume / (total_mass + 1e-6)

        if volume == 0:
            props["rho"] = 0
        else:
            props["rho"] = 1 / props["v"]
        props["m"] = total_mass
        props["NotCalculated"] = comp_not_calculated

        return props

