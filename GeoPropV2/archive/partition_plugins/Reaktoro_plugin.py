from .engine import Engine
from ..partition import factory


def register():
    """
    Registers the Reaktoro partition engine

    Returns
    -------
    NoReturn
    """
    factory.register("reaktoro", Reaktoro)


class Reaktoro(Engine):

    def __init__(self, *args, **kwargs):

        super().__init__(args, kwargs)

    pass