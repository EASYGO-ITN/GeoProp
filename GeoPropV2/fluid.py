from GeoPropV2.constants import PhaseType, Units


class Fluid:

    def __init__(self, *args, units="mol"):

        if not args:
            msg = "No components and their corresponding quanitiy were defined"
            raise ValueError(msg)

        if (len(args) % 2) != 0:
            msg = "Each component must be paired with a quantity"
            raise ValueError(msg)

        components = []
        quantity = []
        for i in range(int(len(args)/2)):
            components.append(args[2*i])
            quantity.append(args[2*i + 1])

        self.total = TotalPhase(components, quantity, Units(units))

        self.solid = EmptyPhase()
        self.aqueous = EmptyPhase()
        self.vapour = EmptyPhase()
        self.element = EmptyPhase()


class Phase:

    def __init__(self, components, quantity, units):

        self.components = components
        self.amount = sum(quantity)
        self.composition = [i/self.amount for i in quantity]
        self.comp_dict = {components[i]: quantity[i] for i in range(len(components))}
        self.units = units

        self.pure = False
        if len(components) == 1:
            self.pure = True

    def phase_type(self):

        return self.__type


class TotalPhase(Phase):

    def __init__(self, components, quantity, units):
        super().__init__(components, quantity, units)

        self.__type = PhaseType.TOTAL

    def phase_type(self):

        return self.__type


class SolidPhase(Phase):

    def __init__(self, components, quantity, units):
        super().__init__(components, quantity, units)

        self.__type = PhaseType.SOLID

    def phase_type(self):

        return self.__type


class AqueousPhase(Phase):

    def __init__(self, components, quantity, units):
        super().__init__(components, quantity, units)

        self.__type = PhaseType.AQUEOUS

    def phase_type(self):

        return self.__type


class VapourPhase(Phase):

    def __init__(self, components, quantity, units):
        super().__init__(components, quantity, units)

        self.__type = PhaseType.VAPOUR

    def phase_type(self):

        return self.__type


class ElementPhase(Phase):

    def __init__(self, components, quantity, units):
        super().__init__(components, quantity, units)

        self.__type = PhaseType.ELEMENT

    def phase_type(self):

        return self.__type


class EmptyPhase(Phase):

    def __init__(self):
        super().__init__(["None"], [1.0], Units.MOL)

        self.__type = PhaseType.NONE

    def phase_type(self):

        return self.__type


#
#
# class Fluid:
#
#     def __init__(self, *args, type="mol"):
#
#         if not args:
#             msg = "No components and their corresponding quanitiy were defined"
#             raise ValueError(msg)
#
#         if (len(args) % 2) != 0:
#             msg = "Each component must be paired with a quantity"
#             raise ValueError(msg)
#
#         self.total = TotalPhase()
#         self.solid = SolidPhase()
#         self.aqueous = AqueousPhase()
#         self.vapour = VapourPhase()
#         self.element = ElementPhase()
#
#         components = []
#         composition = []
#         for i in range(int(len(args)/2)):
#             components.append(args[i])
#             composition.append(args[i+1])
#
#         self.components = components
#         self.composition = composition
#         self.comp_dict = {components[i]: composition[i] for i in range(len(components))}
#         self.units = Units(type)


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

        # creates a variable for each of the items in props
        vars = (i for i in props)

        # assigns the value to each property
        for i in vars:
            setattr(self, i, props[i])

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

    # def __str__(self):
    #     """
    #         Determines the string representation of PhaseProperties objects
    #
    #         Returns
    #         -------
    #         text : str
    #             text string that encompasses all relevant information about the Fluid object
    #     """
    #
    #     text = "P: {:.4e} Pa\tT: {} K\th: {:.4e} kJ/kg\t\ts: {:.4e} kJ/kg/K\trho: {:.4e} kg/m3\tv: {:.4} m3/kg\tm: {:.4e} kg".format(self.P, self.T, self.h, self.s, self.rho, self.v, self.m)
    #     if self.NotCalculated:
    #         text += "\nThe following components were not calculated: {}".format(self.NotCalculated)
    #
    #     return text
    #
    # def copy(self):
    #
    #     newProps = {"P": 0.0, "T": 0.0, "h": 0.0, "s": 0.0, "rho": 0.0, "m": 0.0, "v":0.0}
    #     newProps = {i: self[i]*1.0 for i in newProps}
    #
    #     if self.NotCalculated:
    #         newProps["NotCalculated"] = [i for i in self.NotCalculated]
    #     else:
    #         newProps["NotCalculated"] = None
    #
    #     return PhaseProperties(newProps)



