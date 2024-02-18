from .engine import Engine
from ..partition import factory


def register():
    """
    Registers the Spycher Pruess 2009 partition engine

    Returns
    -------
    NoReturn
    """
    factory.register("spycher_pruess_2009", SpycherPruess2009)


class SpycherPruess2009(Engine):

    def __init__(self, *args, **kwargs):

        super().__init__(args, kwargs)
