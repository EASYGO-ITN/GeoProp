from .Fluid import Fluid
from .PartitionModel import Partition, PartitionModelOptions
from .PropertyModel import PropertyModel, PropertyModelOptions
from .Utilities import RootFinder

import time


class State:
    """
    a class to orchestrate the calculations to equilibrate a state and find the fluid properties
    """

    def __init__(self, part_options=None, prop_options=None):
        """
        initialises the State object

        Parameters
        ----------
        part_options: PartitionModelOptions
            the calculation options to be used for the partition calculations
        prop_options: PropertyModelOptions
            the calculation options to be used for the property calculations
        """

        if part_options is None:
            self.part_options = PartitionModelOptions()
        else:
            self.part_options = part_options

        if prop_options is None:
            self.prop_options = PropertyModelOptions()
        else:
            self.prop_options = prop_options

    def calc_PT(self, fluid, P, T):
        """
        calculates the state of the fluid given an input of pressure and temperature

        Parameters
        ----------
        fluid: Fluid
            the fluid to be calculated
        P: float
            the pressure
        T: float
            the temperature

        Returns
        -------
        Fluid

        """

        fluid = Partition(options=self.part_options).calc(fluid, P, T)

        fluid = PropertyModel(options=self.prop_options).calc(fluid, P, T)

        return fluid

    def calc_Ph(self, fluid, P, h, Tguess=298.0):
        """
        calculates the state of the fluid given an input of pressure and specific enthalpy

        Parameters
        ----------
        fluid: Fluid
            the Fluid to be calculated
        P: float
            the pressure
        h: float
            the specific enthalpy
        Tguess: float
            a guess of the temperature

        Returns
        -------
        Fluid

        """

        a = False

        def ph_search_t(target, t, p):
            temp_fluid = self.calc_PT(fluid, p, t)

            if a:
                print(temp_fluid.gaseous)
                print(temp_fluid.aqueous)

            h_mass = temp_fluid.total.props["h"]

            return target - h_mass

        if self.part_options.model == self.part_options.PartitionModels.SPYCHERPRUSS:
            Tmin = self.part_options.model.value.Tmin
            Tmax = self.part_options.model.value.Tmax

            T = RootFinder.Brent(ph_search_t, h, Tmin, Tmax, others=P)
        else:
            T = RootFinder.Secant(ph_search_t, h, Tguess, Tguess + 10, others=P)

        fluid = self.calc_PT(fluid, P, T)

        return fluid

    def calc_Ps(self, fluid, P, s, Tguess=298.0):
        """
        calculates the state of the fluid given an input of pressure and specific entropy

        Parameters
        ----------
        fluid: Fluid
            the Fluid to be calculated
        P: float
            the pressure
        s: float
            the specific entropy
        Tguess: float
            a guess of the temperature

        Returns
        -------
        Fluid

        """

        def ps_search_t(target, t, p):

            temp_fluid = self.calc_PT(fluid, p, t)
            s_mass = temp_fluid.total.props["s"]

            return target - s_mass

        if self.part_options.model == self.part_options.PartitionModels.SPYCHERPRUSS:
            Tmin = self.part_options.model.value.Tmin
            Tmax = self.part_options.model.value.Tmax

            T = RootFinder.Brent(ps_search_t, s, Tmin, Tmax, others=P)
        else:
            T = RootFinder.Secant(ps_search_t, s, Tguess, Tguess + 10, others=P)

        fluid = self.calc_PT(fluid, P, T)

        return fluid

    def calc_Px(self, fluid, P, x, Tguess= 298.0):

        """
        calculates the state of the fluid given an input of pressure and vapour quality

        Parameters
        ----------
        fluid: Fluid
            the Fluid to be calculated
        P: float
            the pressure
        s: float
            the specific entropy
        Tguess: float
            a guess of the temperature

        Returns
        -------
        Fluid

        """

        def px_search_t(target, t, p):

            temp_fluid = self.calc_PT(fluid, p, t)

            n_vap = sum([temp_fluid.gaseous.moles[i] for i in temp_fluid.gaseous.components])
            n_tot = sum([temp_fluid.total.moles[i] for i in temp_fluid.total.components])

            x = n_vap / n_tot

            return target - x

        if self.part_options.model == self.part_options.PartitionModels.SPYCHERPRUSS:
            Tmin = self.part_options.model.value.Tmin
            Tmax = self.part_options.model.value.Tmax

            T = RootFinder.Brent(px_search_t, x, Tmin, Tmax, others=P)
        else:
            T = RootFinder.Secant(px_search_t, x, Tguess, Tguess + 10, others=P)

        fluid = self.calc_PT(fluid, P, T)

        return fluid
