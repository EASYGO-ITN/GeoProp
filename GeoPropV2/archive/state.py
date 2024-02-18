from .partition.engine import get_partition_engine
from .property.engine import get_property_engine

from .model.engine import *


class State:

    def __init__(self, config):

        if "partition_options" not in config:
            config["partition_options"] = None
        self.partition_engine = get_partition_engine(config["partition"], config["partition_options"])

        if "property_options" not in config:
            config["property_options"] = None
        self.property_engine = get_property_engine(config["property"], config["property_options"])

    def update(self, P, T, fluid):

        temp_fluid = self.partition_engine.calc(P, T, fluid)

        temp_fluid = self.property_engine.calc(P, T, temp_fluid)

        return temp_fluid

