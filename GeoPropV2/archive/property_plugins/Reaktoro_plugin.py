from .engine import Engine
from ..property import factory


def register():
    """
    Registers the Reaktoro partition engine

    Returns
    -------
    NoReturn
    """
    factory.register("reaktoro", ReaktoroEngine)


class ReaktoroEngine(Engine):

    def __init__(self, *args, **kwargs):

        super().__init__(args, kwargs)

    pass