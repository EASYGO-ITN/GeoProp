from .Fluid import Fluid
from .Blender import Blender
from .PropertyModel import PhaseProperties, PropertyModel

from typing import Union, Optional
from enum import Enum


class Recombination:

    @staticmethod
    def byVolume(fluid1, fluid2, Pref, Tref, VolRatio):

        fluid1.normaliseComposition()
        fluid2.normaliseComposition()

        fluid1 = PropertyModel().calc(fluid1, Pref, Tref)
        fluid2 = PropertyModel().calc(fluid2, Pref, Tref)

        MassRatio = VolRatio / ((fluid2.total.props.v * fluid2.total.props.m) / (fluid1.total.props.v * fluid1.total.props.m))

        return Blender.blend(fluid1, fluid2, ratio2to1=MassRatio)

    @staticmethod
    def byMass(fluid1, fluid2, MassRatio):

        fluid1.normaliseComposition()
        fluid2.normaliseComposition()

        return Blender.blend(fluid1, fluid2, ratio2to1=MassRatio)

    @staticmethod
    def byMole(fluid1, fluid2, MoleRatio):

        fluid1.normaliseComposition()
        fluid2.normaliseComposition()

        total_moles1 = sum([fluid1.total.moles[i] for i in fluid1.total.components])
        total_moles2 = sum([fluid2.total.moles[i] for i in fluid2.total.components])

        MassRatio = MoleRatio / (total_moles2 / total_moles1)

        return Blender.blend(fluid1, fluid2, ratio2to1=MassRatio)