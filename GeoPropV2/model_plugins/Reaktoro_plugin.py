from .BaseModel import Model
from ..model import factory


def register():
    """
    Registers the Reaktoro partition engine

    Returns
    -------
    NoReturn
    """
    factory.register("reaktoro", ReaktoroModel)


class ReaktoroModel(Model):

    _partition = True
    _properties = True
    _properties_solid = True
    _properties_aqueous = True
    _properties_vapour = True

    def __init__(self, *args, **kwargs):

        super().__init__(args, kwargs)

    pass