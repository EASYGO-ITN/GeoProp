from . import models


def get_model(model, options):

    if model not in models:
        string_models = ','.join(mod for mod in models)
        msg = "The specified model \"{}\" is not recognised. The following models are available: " + string_models + "."
        raise ValueError(msg)

    return models[model](model, options=options)
