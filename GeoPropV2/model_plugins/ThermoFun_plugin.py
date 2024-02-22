import thermofun as tf
import CoolProp as cp
import os

from .BaseModel import Model
from ..model import factory
from GeoPropV2.constants import Units, PhaseType
from GeoPropV2 import Pref, Tref
from GeoPropV2.fluid import PhaseProperties


def register():
    """
    Registers the Reaktoro partition engine

    Returns
    -------
    NoReturn
    """
    factory.register("thermofun", ThermoFunModel)


class ThermoFunModel(Model):

    _partition = False
    _properties = True
    _properties_solid = True
    _properties_aqueous = True
    _properties_vapour = False

    properties = ["D", "V", "Q", "H", "S"]

    _molar_masses = {"H2O": 0.01801528}

    def __init__(self, *args, options={}, **kwargs):

        super().__init__(args, kwargs)

        self.__initialised = False
        self.__state = None

        self.__h0 = 0.0
        self.__s0 = 0.0

        default_opts = {"database": "slop98-inorganic-thermofun.json"}  # add further options to this
        if options:
            for opt in options:
                default_opts[opt] = options[opt]

        self.__database_name = default_opts["database"]

    def init_properties(self, fluid, phase):

        data_base_dir = os.path.dirname(__file__)+"\\thermofun_databases"
        database = data_base_dir + "\\" + self.__database_name

        self.__engine = tf.ThermoEngine(database)
        self.__database = tf.Database(database)
        self.__water = cp.AbstractState("?", "Water")
        self.__water.update(cp.PT_INPUTS, Pref, Tref)
        self.__water_h0 = self.__water.hmass()
        self.__water_s0 = self.__water.smass()

        self.__initialised = True

    def calc_properties(self, P, T, fluid, phase):

        if not self.__initialised:

            self.init_properties(fluid, phase)

        enthalpy = 0
        entropy = 0
        volume = 0
        mass = 0
        not_calculated = []

        for i, comp in enumerate(fluid.components):

            if comp in ["Water", "H2O"]:
                if phase == PhaseType.AQUEOUS:
                    self.__water.update(cp.PT_INPUTS, P, T)

                    if fluid.units == Units.MASS:
                        m = fluid.composition[i] * fluid.amount
                    else:
                        m = fluid.composition[i] * fluid.amount * self._molar_masses["H2O"]
                    mass += m
                    enthalpy += (self.__water.hmass() - self.__water_h0) * m
                    entropy += (self.__water.smass() - self.__water_s0) * m
                    volume += m / self.__water.rhomass()
                else:
                    msg = "ThermoFun only permits evaluation of H2O in the liquid state"
                    raise ValueError(msg)
            else:

                if phase == PhaseType.AQUEOUS:
                    comp_name = comp*1

                    if "(aq)" in comp_name:
                       comp_name.replace("(aq)", "@")
                    elif "+" not in comp_name and "-" not in comp_name:
                        comp_name += "@"

                try:
                    substance = self.__database.getSubstance(comp_name)
                    Mr = substance.molarMass() * 1e-3
                except:
                    not_calculated.append(comp)
                else:
                    properties = self.__engine.thermoPropertiesSubstance(T, P, comp_name)
                    properties0 = self.__engine.thermoPropertiesSubstance(Tref, Pref, comp_name)

                    if fluid.units == Units.MASS:
                        m = fluid.composition[i] * fluid.amount
                        mass += m

                    else:
                        m = fluid.composition[i] * fluid.amount * Mr
                        mass += m
                        enthalpy += m * (properties.enthalpy.val - properties0.enthalpy.val) / Mr  # the units of enthalpy are J/mol
                        entropy += m * (properties.entropy.val - properties0.entropy.val) / Mr  # the units of entropy are J/mol
                        volume += m * properties.volume.val * 1e-5 / Mr

        results = {}
        for prop in self.properties:
            match prop:
                case "D":
                    results[prop] = mass/(volume + 1e-15)
                case "V":
                    results[prop] = volume / (mass + 1e-15)
                case "H":
                    results[prop] = enthalpy / (mass + 1e-15)
                case "S":
                    results[prop] = entropy / (mass + 1e-15)

        fluid.props = PhaseProperties(results)

