from enum import Enum
import CoolProp as cp
from CoolProp.CoolProp import PropsSI

from .BaseModel import Model
from ..model import factory
from GeoPropV2.constants import Units, PhaseType
from GeoPropV2 import Pref, Tref
from GeoPropV2.fluid import PhaseProperties, AqueousPhase, VapourPhase


def register():
    """
    Registers the Reaktoro partition engine

    Returns
    -------
    NoReturn
    """
    factory.register("coolprop", CoolPropModel)

# class Properties(Enum):
#     DENSITY = "D"
#     VOLUME = "V"
#     QUALITY = "Q"
#     ENTHALPY = "H"
#     ENTROPY = "S"


class CoolPropModel(Model):

    _partition = True
    _properties = True
    _properties_solid = False
    _properties_aqueous = True
    _properties_vapour = True

    properties = ["D", "V", "Q", "H", "S"]

    def __init__(self, *args, options={}, **kwargs):

        super().__init__(args, kwargs)

        self.__initialised = False
        self.__state = None

        self.__h0 = 0.0
        self.__s0 = 0.0

        default_opts = {"backend": "?"}# add further options to this
        if options:
            for opt in options:
                default_opts[opt] = options[opt]

        self.__backend = default_opts["backend"]

    def init_partition(self, fluid):

        self.__init_state(fluid.total)

        self.__initialised = True

    def calc_partition(self, P, T, fluid):

        if not self.__initialised:

            self.init_partition(fluid)

        self.__calc_state(P, T)

        # calculate alpha - the vapour fraction
        alpha = -1
        phase = self.__state.phase()
        if phase in [cp.iphase_twophase]:
            alpha = self.__state.Q()
        elif phase in [cp.iphase_liquid, cp.iphase_supercritical_liquid]:
            alpha = 0
        elif phase in [cp.iphase_gas, cp.iphase_supercritical, cp.iphase_supercritical_gas]:
            alpha = 1
        elif phase in [cp.iphase_critical_point]:
            alpha = 0.5
        else:
            msg = "Calculated phase \"{}\" not recognised".format(phase)
            raise ValueError(msg)

        # define the components for the new phases
        liq_comps = [x for x in fluid.total.components]
        vap_comps = [x for x in fluid.total.components]

        # define the compositions of the new phases
        if fluid.total.pure:
            liq_quant = [1]
            vap_quant = [1]

            # conversion of alpha between mass and mol is not required as the fluid is pure

        else:
            if 0 < alpha < 1:
                liq_quant = self.__state.mole_fractions_liquid()
                vap_quant = self.__state.mole_fractions_vapor()

                if fluid.total.units == Units.MASS:
                    # TODO some conversion from mol to mass if required.. including alpha
                    pass

            else:
                if fluid.total.units == Units.MOL:
                    liq_quant = self.__state.get_mole_fractions()
                    vap_quant = self.__state.get_mole_fractions()
                else:
                    liq_quant = self.__state.get_mass_fractions()
                    vap_quant = self.__state.get_mass_fractions()

        fluid.aqueous = AqueousPhase(liq_comps, liq_quant, fluid.total.units)
        fluid.vapour = VapourPhase(vap_comps, vap_quant, fluid.total.units)

    def init_properties(self, fluid, phase):

        self.__init_state(fluid)

        try:
            self.__state.update(cp.PT_INPUTS, Pref, Tref)
        except:
            # TODO need to issue a warning if the calculation has not been able to initialise

            if phase == PhaseType.AQUEOUS:
                try:
                    self.__state.update(cp.QT_INPUTS, 0, Tref)
                except:
                    self.__state.update(cp.PQ_INPUTS, Pref, 0)

            elif phase == PhaseType.VAPOUR:
                try:
                    self.__state.update(cp.QT_INPUTS, 1, Tref)
                except:
                    self.__state.update(cp.PQ_INPUTS, Pref, 1)

        self.__h0 = self.__state.hmass()
        self.__s0 = self.__state.smass()

        self.__initialised = True

    def calc_properties(self, P, T, fluid, phase):

        if not self.__initialised:

            self.init_properties(fluid, phase)

        try:
            self.__state.update(cp.PT_INPUTS, P, T)
        except:
            if phase == PhaseType.AQUEOUS:
                try:
                    self.__state.update(cp.QT_INPUTS, 0, T)
                except:
                    self.__state.update(cp.PQ_INPUTS, P, 0)

            elif phase == PhaseType.VAPOUR:
                try:
                    self.__state.update(cp.QT_INPUTS, 1, T)
                except:
                    self.__state.update(cp.PQ_INPUTS, P, 1)

        fluid.props = self.__get_properties()

    def __init_state(self, fluid):

        component_string = ""
        molar_masses = []
        for comp in fluid.components:
            try:
                cp.CoolProp.get_fluid_param_string(comp, "name")
            except:
                msg = "The component {} is not recognised in CoolProp".format(comp)
                raise ValueError(msg)
            component_string += comp + "&"
            molar_masses.append(PropsSI("M", comp))

        # create the CoolProp Abstract state
        self.__state = cp.AbstractState(self.__backend, component_string[:-1])

        # if multi components set the base mol or mass fractions
        if len(fluid.composition) > 1:
            if fluid.units == Units.MOL:
                self.__state.set_mole_fractions(fluid.composition)
            elif fluid.units == Units.MASS:
                self.__state.set_mass_fractions(fluid.composition)
            else:
                msg = "The fluid units, \"{}\" have not been recognised".format(fluid.units)
                raise ValueError(msg)

    def __calc_state(self, P, T):

        self.__state.update(cp.PT_INPUTS, P, T)

    def __get_properties(self):

        results = {}
        for prop in self.properties:
            match prop:
                case "D":
                    results[prop] = self.__state.rhomass()
                case "V":
                    results[prop] = 1 / self.__state.rhomass()
                case "H":
                    results[prop] = self.__state.hmass() - self.__h0
                case "S":
                    results[prop] = self.__state.smass() - self.__s0

        return PhaseProperties(results)