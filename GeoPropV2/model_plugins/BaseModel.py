class Model:

    _partition = False
    _properties = False
    _properties_solid = False
    _properties_aqueous = False
    _properties_vapour = False

    def __init__(self, *args, **kwargs):

        pass

    def calc(self, P, T, fluid, *args, **kwargs):

        pass

    def calc_partition(self, P, T, fluid):

        pass

    def init_partition(self, fluid):

        pass

    def calc_properties(self, P, T, fluid, phase):

        pass

    def init_properties(self, fluid, phase):

        pass

