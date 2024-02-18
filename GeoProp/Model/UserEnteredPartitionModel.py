import copy
from typing import List, Union, Dict, Tuple, NoReturn, Optional


class UserPartitionOptions:
    """
         the UserPartionOptions class contains the options for the UserPartition calculation
    """

    pass


class UserPartition:

    @staticmethod
    def calc(fluid, P, T, options):
        print("User Partition")
        return copy.deepcopy(fluid)
