from .BaseModel import Model
from ..model import factory


def register():
    """
    Registers the Reaktoro partition engine

    Returns
    -------
    NoReturn
    """
    factory.register("thermofun", ThermoFunModel)


class ThermoFunModel(Model):

    _partition = False
    _properties = True
    _properties_solid = True
    _properties_aqueous = True
    _properties_vapour = False

    def __init__(self, *args, **kwargs):

        super().__init__(args, kwargs)

    pass