from .UserEnteredPartitionModel import UserPartition, UserPartitionOptions
from .ReaktoroPartitionModel import ReaktoroPartition, ReaktoroPartitionOptions
from .SpycherPruessPartitionModel import SpycherPrussPartition
from .Fluid import Fluid

from enum import Enum
from typing import Union, Optional


class PartitionModelOptions:
    """
    The settings governing the partition calculations.

    Attributes
    ----------
    model : PartitionModels
        the partition model to be used
    UserEntered : UserPartitionOptions
        the partition model options for UserEntered partitions
    Reaktoro : ReaktoroPartitionOptions
        the partition model options  Reaktoro partitions

    """

    class PartitionModels(Enum):
        USER_ENTERED = UserPartition
        REAKTORO = ReaktoroPartition
        SPYCHERPRUSS = SpycherPrussPartition


    def __init__(self):
        self.model = self.PartitionModels.REAKTORO

        self.UserEntered = UserPartitionOptions()
        self.Reaktoro = ReaktoroPartitionOptions()
        self.SpycherPruss = None


class Partition:
    """
    The Partition class handles the distribution of partition calculations to the selected partition model.

    Attributes
    ----------
    options : PartitionModelOptions
        the calculation options to be used for the partition
    partitionModel : PartitionModelOptions.PartitionModels

    """

    def __init__(self, options: Optional[PartitionModelOptions] = PartitionModelOptions()):
        """
        Initialises a Partition object from partitioning options (optional)

        Parameters
        ----------
        options (opt): PartitionModelOptions
            the calculation options to be used for the partition

        """

        self.options = options
        self.partitionModel = options.model

    def calc(self, fluid: Fluid, P: float, T: float) -> Fluid:
        """
        executes the partition calculation witht he selected partition model

        Parameters
        ----------
        fluid : Fluid
            the fluid to be partitioned
        P : Union[int, float]
            the pressure in Pa
        T : Union[int, float]
            the temperature in K

        Returns
        -------
        Fluid
            the partitioned fluid
        """

        # reset the phase properties flag
        fluid.total.props_calculated = False
        fluid.aqueous.props_calculated = False
        fluid.gaseous.props_calculated = False
        fluid.mineral.props_calculated = False

        # set the correct options for the partition model
        if self.partitionModel == PartitionModelOptions.PartitionModels.REAKTORO:
            options = self.options.Reaktoro
        elif self.partitionModel == PartitionModelOptions.PartitionModels.SPYCHERPRUSS:
            options = self.options.SpycherPruss
        else:
            options = self.options.UserEntered

        return self.partitionModel.value.calc(fluid, P, T, options)
