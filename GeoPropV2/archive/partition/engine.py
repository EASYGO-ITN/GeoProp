from . import engines


def get_partition_engine(engine, *args, **kwargs):

    if engine not in engines:
        string_engines = ','.join(eng for eng in engines)
        msg = "The specified model \"{}\" is not recognised. The following engines are available: " + string_engines + "."
        raise ValueError(msg)

    return engines[engine](args, kwargs)
