"""
Constants used throughout the Thermophysical Calculator.

Attributes
----------
Pref : Union[int, float]
    the reference pressure used to calculate changes in enthalpy and entropy
Tref : Union[int, float]
    the reference temperature used to calculate changes in enthalpy and entropy

Raises
------
Nothing
"""

Pref = 101325  # reference pressure in Pa
Tref = 298  # reference temperature in K

# TODO converting compositions should be handled globally, however this will need a global database of components...