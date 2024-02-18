from .Fluid import Fluid
from .Phases import PhaseProperties

from typing import Union, Optional


class Blender:
    """
    The Blender class allows two Fluids to be mixed

    Attributes
    ----------
    None

    """

    @staticmethod
    def blend(fluid1: Fluid, fluid2: Fluid, ratio2to1: Optional[float] = 1.0) -> Fluid:
        """
        Mixes two fluids according to a mass-based mixing ration.

        Parameters
        ----------
        fluid1 : Fluid
            the first Fluid to be mixed
        fluid2 : Fluid
            the second Fluid to be mixed
        ratio2to1 : Union[float, int]
            the ratio of the mass of fluid2 to the mass of fluid1

        Returns
        -------
        Fluid
            a Fluid object containing the mixed fluids

        Raises
        ------
        Nothing
        """

        # create copies of the component lists of the two fluids
        components1 = [i for i in fluid1.total.components]
        components2 = [i for i in fluid2.total.components]

        # combine the components, omitting any duplicates
        components = list(set(components1 + components2))

        # find the components that do not exist in the parent fluid
        diff1 = list(set(components) - set(components1))
        diff2 = list(set(components) - set(components2))

        # buff out the mass dictionaries of each fluid to also contain the new components
        mass1 = {i:fluid1.total.mass[i] for i in fluid1.total.mass}
        for comp in diff1:
            mass1[comp] = 0
        mass2 = {i:fluid2.total.mass[i] for i in fluid2.total.mass}
        for comp in diff2:
            mass2[comp] = 0

        # create the composition list
        composition = [0 for i in components]
        for i, comp in enumerate(components):
            composition[i] = mass1[comp] + ratio2to1 * mass2[comp]

        # create the new fluid from the component and composition lists
        new_fluid = Fluid(components=components, composition=composition)

        # if the properties were calculated for the same pressure and temperature, update the property results
        if fluid1.total.props_calculated and fluid2.total.props_calculated:
            if fluid1.total.props["P"] == fluid2.total.props["P"] and fluid1.total.props["T"] == fluid2.total.props["T"]:

                # repeat for all other phases
                for phase in new_fluid.total.phases:

                    # check if the parent fluids share a given phase
                    if phase in fluid1.total.phases and phase in fluid2.total.phases and fluid1.total.phases[phase].props.m > 0 and fluid2.total.phases[phase].props.m > 0:
                        phase1 = fluid1.total.phases[phase]
                        phase2 = fluid2.total.phases[phase]

                        not_calculated = []
                        if phase1.props["NotCalculated"] is not None and phase2.props["NotCalculated"] is not None:
                            not_calculated = phase1.props["NotCalculated"] + phase2.props["NotCalculated"]
                        elif phase1.props["NotCalculated"] is not None:
                            not_calculated = phase1.props["NotCalculated"]
                        else:
                            not_calculated = phase2.props["NotCalculated"]

                        # calculate the combined properties
                        props = {"P": fluid1.total.props["P"],
                                 "T": fluid1.total.props["T"],
                                 "h": (phase1.props["m"] * phase1.props["h"] + ratio2to1 * phase2.props["m"] * phase2.props["h"]) / (phase1.props["m"] + ratio2to1 * phase2.props["m"]),
                                 "s": (phase1.props["m"] * phase1.props["s"] + ratio2to1 * phase2.props["m"] * phase2.props["s"]) / (phase1.props["m"] + ratio2to1 * phase2.props["m"]),
                                 "rho": (phase1.props["m"] + ratio2to1 * phase2.props["m"]) / ((phase1.props["m"] / (phase1.props["rho"] + 1e-6)) + (ratio2to1 * phase2.props["m"] / (phase2.props["rho"] + 1e-6))),
                                 "v": (phase1.props["m"] * phase1.props["v"] + ratio2to1 * phase2.props["m"] * phase2.props["v"]) / (phase1.props["m"] + ratio2to1 * phase2.props["m"]),
                                 "m": phase1.props["m"] + ratio2to1 * phase2.props["m"],
                                 "NotCalculated": not_calculated
                                 }
                    else:
                        props = {"P": fluid1.total.props["P"]*1.0,
                                 "T": fluid1.total.props["T"]*1.0}

                        if phase in fluid1.total.phases and fluid1.total.phases[phase].props.m > 0:
                            phase_ = fluid1.total.phases[phase]
                            props["m"] = phase_.props["m"]*1.0
                        else:
                            phase_ = fluid2.total.phases[phase]
                            props["m"] = phase_.props["m"]*ratio2to1

                        props["h"] = phase_.props["h"]*1.0
                        props["s"] = phase_.props["s"]*1.0
                        props["rho"] = phase_.props["rho"]*1.0
                        props["v"] = phase_.props["v"]*1.0
                        props["NotCalculated"] = phase_.props["NotCalculated"]

                    # create new phase properties
                    new_fluid.total.phases[phase].props = PhaseProperties(props)

                    # set flag
                    new_fluid.total.phases[phase].props_calculated = True

                new_fluid._totalPhaseProps()

        # return the new fluid
        return new_fluid



