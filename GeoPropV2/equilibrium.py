from .model.engine import get_model

from GeoPropV2.constants import PhaseType


class State:

    def __init__(self, config):

        if "partition_opts" not in config:
            config["partition_opts"] = None
        self.partition_model = get_model(config["partition"], config["partition_opts"])

        if not self.partition_model._partition:
            msg = "The selected model \"{}\" does not support partition calculations".format(config["partition"])
            raise ValueError(msg)

        if "property_opts" not in config:
            config["property_opts"] = {"solid": None, "aqueous": None, "vapour": None}

        self.property_model = PropertyModel()

        self.property_model.solid_model = get_model(config["property"]["solid"], config["property_opts"]["solid"])
        if not self.property_model.solid_model._properties_solid:
            msg = "The selected model \"{}\" does not support property calculations for SOLID phases".format(config["property"]["solid"])
            raise ValueError(msg)

        self.property_model.aqueous_model = get_model(config["property"]["aqueous"], config["property_opts"]["aqueous"])
        if not self.property_model.aqueous_model._properties_aqueous:
            msg = "The selected model \"{}\" does not support property calculations for AQUEOUS phases".format(config["property"]["aqueous"])
            raise ValueError(msg)

        self.property_model.vapour_model = get_model(config["property"]["vapour"], config["property_opts"]["vapour"])
        if not self.property_model.vapour_model._properties_vapour:
            msg = "The selected model \"{}\" does not support property calculations for VAPOUR phases".format(config["property"]["vapour"])
            raise ValueError(msg)

    def __call__(self, P, T, fluid, *args, **kwargs):

        self.partition_model.calc_partition(P, T, fluid)

        self.property_model.calc(P, T, fluid)


class PropertyModel:

    def __init__(self):

        self.solid_model = None
        self.aqueous_model = None
        self.vapour_model = None

    def calc(self, P, T, fluid):

        solid_props = self.solid_model.calc_properties(P, T, fluid.solid, PhaseType.SOLID)

        aqueous_props = self.aqueous_model.calc_properties(P, T, fluid.aqueous, PhaseType.AQUEOUS)

        vapour_props = self.vapour_model.calc_properties(P, T, fluid.vapour, PhaseType.VAPOUR)

        total_props = None

        return total_props, solid_props, aqueous_props, vapour_props
