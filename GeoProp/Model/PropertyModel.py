from .ThermoFunPropertyModel import ThermoFunProperties, ThermoFunPropertyOptions
from .CoolPropPropertyModel import CoolPropProperties, CoolPropPropertyOptions
from .Fluid import Fluid

from .Phases import PhaseProperties, PhaseType

from enum import Enum
from typing import List, Union, Dict, Tuple, NoReturn, Optional

import time


class PropertyModelOptions:
    """
        The PropertyModelOptions class contains the options of all property model

        Attributes
        ----------
        ThermFun: ThermoFunPropertyOptions
            The calculation options for the ThermoFunPropertyModel
        CoolProp: CoolPropPropertyOptions
            The calculation options for the CoolPropPropertyModel
    """

    # initialises the ThermoFun and CoolProp property model options
    ThermoFun = ThermoFunPropertyOptions()
    CoolProp = CoolPropPropertyOptions()


class PropertyModels(Enum):
    """
        The PropertyModel class contains links to all property model

        Attributes
        ----------
        THERMOFUN: ThermoFunProperties
            The link to the ThermoFunPropertyModel
        COOLPROP: CoolPropProperties
            The link to the CoolPropPropertyModel
    """

    # the different property model available
    THERMOFUN = ThermoFunProperties
    COOLPROP = CoolPropProperties


class PropertyModel:
    """
        The PropertyModel class orchestrates all property calculations

        Attributes
        ----------
        options: PropertyModelOptions
            the calculation options to be used for the property calculations

    """

    def __init__(self, options: Optional[PropertyModelOptions] = PropertyModelOptions()):
        """
            initialises the PropertyModel with the calculation options

            Parameters
            ----------
            options: Optional[PropertyModelOptions]
                the calculation options to be used for the property calculations
        """

        # set the calculation options
        self.options = options

    def calc(self, fluid: Fluid, P: float, T: float) -> Fluid:
        """
            calculates the thermophysical properties of the input fluid

            Parameters
            ----------
            fluid: Fluid
                the fluid whose thermophysical properties should be evaluated
            P: float
                the pressure in Pa
            T: float
                the temperature in K

            Returns
            --------
            fluid: Fluid
                the calculated fluid
        """

        # trigger the property calculations for the aqueous phase
        if fluid.aqueous.components:
            props = PropertyModels.THERMOFUN.value.calc(fluid.aqueous, P, T, self.options.ThermoFun)
            fluid.aqueous.props = PhaseProperties(props)
            fluid.aqueous.props_calculated = True

        # trigger the property calculations for the gaseous phase
        if fluid.gaseous.components:
            props = PropertyModels.COOLPROP.value.calc(fluid.gaseous, P, T, self.options.CoolProp)
            fluid.gaseous.props = PhaseProperties(props)
            fluid.gaseous.props_calculated = True

        # trigger the property calculations for the mineral phase
        if fluid.mineral.components:
            props = PropertyModels.THERMOFUN.value.calc(fluid.mineral, P, T, self.options.ThermoFun)
            fluid.mineral.props = PhaseProperties(props)
            fluid.mineral.props_calculated = True

        fluid._totalPhaseProps()

        return fluid

    def calcChange(self, fluid, P1, T1, P2, T2, phaseType=PhaseType.TOTAL):

        fluid = self.calc(fluid, P1, T1)
        if phaseType == PhaseType.TOTAL:
            props1 = fluid.total.props.copy()
        else:
            props1 = fluid.total.phases[phaseType].props.copy()

        fluid = self.calc(fluid, P2, T2)
        if phaseType == PhaseType.TOTAL:
            props2 = fluid.total.props.copy()
        else:
            props2 = fluid.total.props[phaseType].props.copy()

        props = props1.copy()
        props.P -= props2.P
        props.T -= props2.T
        props.m -= props2.m
        props.v -= props2.v
        props.h -= props2.h
        props.s -= props2.s
        props.rho -= props2.rho

        return props, props1, props2

