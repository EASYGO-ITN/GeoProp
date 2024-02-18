from . import Phases
from typing import List, Union, Dict, Tuple, NoReturn, Optional


class Species:
    """
        the Species class summarises the properties of a chemical species

        Attributes
        ----------
        name: str
            the species name
        alias: Dict
            dictionary of the species alias in Reaktoro and CoolProp
        elements: List[str]
            the elements that make up this species
        Mr: float
            the molecular mass of the species in kg/mol
        charge: int
            the molecular charge of the species in C/mol
        phase: PhaseType
            the phase in which this species resides

    """

    def __init__(self, rkt_name: str, cp_name: Union[str, None], elements: List[str], Mr: float, charge: Union[int, float], phase: Phases.PhaseType):
        """
            initialises the Species object

            Parameters
            ----------
            rkt_name: str
                the species name in the Reaktoro database
            cp_name: Union[str, None]
                the species name in the CoolProp database
            elements: List[str]
                the elements in the species
            Mr: float
                the species molecular weight in kg/mol
            charge: float
                the species charge in C/mol
            phase: PhaseType
                the phase in which this species resides
        """
        self.name = rkt_name
        self.alias = {"RKT": rkt_name, "CP": cp_name}
        self.elements = elements
        self.Mr = Mr
        self.charge = charge
        self.phase = phase

    def __str__(self) -> str:
        """
            Generates the Species object's string representation

            Returns
            -------
            text:str
        """

        # print the species name
        text = "Species Name: {} \n".format(self.name)

        # print the species phase
        text = text + "Phase: {}\n".format(self.phase.value)

        # print the species aliases
        text = text + "Aliases: \n"
        for alias in self.alias:
            text = text + "\t{}: {}\n".format(alias, self.alias[alias])

        # print the elements in a species
        text = text + "Elements:\n"
        for element in self.elements:
            text = text + "\t{}\n".format(element)

        # print the species molecular weight and charge
        text = text + "Molecular Weight: {} kg/mol\n".format(self.Mr)
        text = text + "Charge: {} \n".format(self.charge)

        return text

