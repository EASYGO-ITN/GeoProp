from . import engines


def get_property_engine(engine, options):

    error = []
    for eng in engine:
        if engine[eng] not in engines:
            error.append(engine[eng])

    if error:
        string_error = ", ".join("\"" + err + "\"" for err in error)
        string_engines = ", ".join("\"" + eng + "\"" for eng in engines)

        msg = "The specified model(s): {} is not recognised. The following engines are available: {}.".format(string_error, string_engines)
        raise ValueError(msg)

    solid, aqueous, vapour = engine["solid"], engine["aqueous"], engine["vapour"]
    solid_opts, aqueous_opts, vapour_opts = options["solid"], options["aqueous"], options["vapour"]

    return PropertyEngine(solid, solid_opts, aqueous, aqueous_opts, vapour, vapour_opts)


class PropertyEngine:

    def __init__(self, solid, solid_opts, aqueous, aqueous_opts, vapour, vapour_opts,):

        self.solid = engines[solid](solid_opts)
        self.aqueous = engines[aqueous](aqueous_opts)
        self.vapour = engines[vapour](vapour_opts)

    def calc(self, P, T, fluid):

        solid_props = self.solid.calc(P, T, fluid.solid)

        aqueous_props = self.aqueous.calc(P, T, fluid.aqueous)

        vapour_props = self.vapour.calc(P, T, fluid.vapour)

        pass


