from .Constants import *
from .Phases import Phase

import CoolProp as cp
from typing import Dict


class CoolPropPropertyOptions:
    """
    The settings governing the calculation of fluid properties from CoolProp.

    Attributes
    ----------
    massfracCutOff : float
        the minimum mass fraction for a component to be considered in the property calculations
    """

    def __init__(self):
        self.massfracCutOff = 1e-6


class CoolPropProperties:
    """
    The CoolPropProperties class handles the calculation of fluid properties using CoolProp.

    """

    @staticmethod
    def calc(phase: Phase, P: float, T: float, options: CoolPropPropertyOptions) -> Dict:
        """
        Calculates the properties of a phase (gaseous) at a given temperature and pressure.

        Parameters
        ----------
        phase : Phase
            the (gaseous) phase storing the composition
        P : Union[int, float]
            the pressure in Pa
        T : Union[float, int]
            the temperature in K

        Returns
        -------
        Dict
            a dictionary of the fluid properties

        Raises
        ------
        Nothing
        """

        # initialise the property results
        props = {"P": 0, "T": 0, "h": 0, "s": 0, "rho": 0, "v": 0, "m": 0, "NotCalculated": []}

        # create the input name string and mass fraction list for CoolProp
        components = ""
        mass_fracs = []
        mole_frac = []
        for i, comp in enumerate(phase.components):
            if phase.massfrac[i] > options.massfracCutOff:
                components += comp.value.alias["CP"] + "&"  # add the component name to the components name string
                mass_fracs.append(phase.massfrac[i])  # add the component mass fraction to the list
                mole_frac.append(phase.molefrac[i])  # add the component mole fraction to the list

        # format the CoolProp inputs
        components = components[:-1]  # remove the final "&"
        mass_fracs = [i/sum(mass_fracs) for i in mass_fracs]  # rescale the mass_fractions to ensure they add up to 1

        # check that there are components in the gas phase left
        if components:

            # create a CoolProp calculation instance for the components
            calc = cp.AbstractState("?", components)

            # check if there are multiple components in the mixture
            if len(components.split("&")) > 1:
                # may need something to check that the BIC data exists.

                # set the mass fractions
                calc.set_mass_fractions(mass_fracs)

            try:

                # calculate the fluid at the reference state
                calc.update(cp.PT_INPUTS, Pref, Tref)
                h0 = calc.hmass()
                s0 = calc.smass()

                # calculate the fluid at the pressure and temperature of interest
                Tsat = T
                try:
                    calc.update(cp.PQ_INPUTS, P, 1.0)
                    Tsat = calc.T()

                except:
                    calc.update(cp.PT_INPUTS, P, T)

                if abs(Tsat - T)/T > 0.01:
                    calc.update(cp.PT_INPUTS, P, T)

                # retrieve the enthalpy, entropy and volume data
                enthalpy = (calc.hmass() - h0)
                entropy = (calc.smass() - s0)
                volume = 1 / calc.rhomass()

            except ValueError:
                # if for some reason CoolProp cannot calculate the mixture, perform the calculations individually and
                # then recombine the results

                # split the component string into its components
                components = components.split("&")

                # initialise the properties
                enthalpy = 0
                entropy = 0
                volume = 0
                for i, comp in enumerate(components):
                    # initialise the CoolProp calculation instance for the component
                    calc = cp.AbstractState("?", comp)

                    # calculate the properties at the reference state
                    calc.update(cp.PT_INPUTS, Pref * mole_frac[i], Tref)
                    h0 = calc.hmass()
                    s0 = calc.smass()

                    # calculate the properties at the pressure and temperature of interest
                    calc.update(cp.PT_INPUTS, P* mole_frac[i], T)

                    # retrieve the results
                    enthalpy += (calc.hmass() - h0) * mass_fracs[i]
                    entropy += (calc.smass() - s0) * mass_fracs[i]
                    volume += mass_fracs[i] / calc.rhomass()

            # update the fluid properties in the properties dictionary
            total_mass = sum([phase.mass[i] for i in phase.mass])
            props["P"] = P
            props["T"] = T
            props["h"] = enthalpy / 1e3
            props["s"] = entropy / 1e3
            props["rho"] = 1 / (volume + 1e-15)
            props["v"] = volume
            props["m"] = total_mass
            props["NotCalculated"] = None

        return props

