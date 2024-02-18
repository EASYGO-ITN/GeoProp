from typing import Callable, NoReturn
from ..property_plugins.engine import Engine

engine_creation_funcs: dict[str, Callable[..., Engine]] = {}


def register(engine_name: str, creation_func: Callable[..., Engine]) -> NoReturn:
    """
    Register a new calculation engine

    Parameters
    ----------
    engine_name: str
        name of the engine to be registered
    creation_func: Callable[..., Engine]
        function that instantiates the engine
    Returns
    -------
    NoReturn
    """

    engine_creation_funcs[engine_name] = creation_func


def unregister(engine_name: str) -> NoReturn:
    """
    Unregister a calculation engine.

    Parameters
    ----------
    engine_name: str
        name of the engine to be unregistered
    Returns
    -------
    NoReturn

    """
    engine_creation_funcs.pop(engine_name, None)


def create(arguments: dict[str, any]) -> Callable[..., Engine]:
    """
    Create a calculation engine given JSON data.

    Parameters
    ----------
    arguments: dict
        the arguments required for creating an engine

    Returns
    -------
    Callable
        the function for instantiating an engine

    Raises
    ------
    ValueError
        if engine type is not a registered engine

    """
    args_copy = arguments.copy()
    engine_type = args_copy.pop("type")
    try:
        creator_func = engine_creation_funcs[engine_type]
    except KeyError:
        raise ValueError(f"unknown engine type {engine_type!r}") from None
    return creator_func