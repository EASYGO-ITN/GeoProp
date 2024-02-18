from typing import Callable, NoReturn
from ..model_plugins.BaseModel import Model

model_creation_funcs: dict[str, Callable[..., Model]] = {}


def register(model_name: str, creation_func: Callable[..., Model]) -> NoReturn:
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

    model_creation_funcs[model_name] = creation_func


def unregister(model_name: str) -> NoReturn:
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
    model_creation_funcs.pop(model_name, None)


def create(arguments: dict[str, any]) -> Callable[..., Model]:
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
    model_name = args_copy.pop("name")
    try:
        creator_func = model_creation_funcs[model_name]
    except KeyError:
        raise ValueError(f"unknown model name {model_name!r}") from None
    return creator_func