import importlib


class ModuleInterface:
    """Represents a plugin interface. A plugin has a single register function."""

    @staticmethod
    def register():
        """Register the necessary items in the game character factory."""


def import_module(name):
    """Imports a module given a name."""
    return importlib.import_module(name, "GeoPropV2")


def load_plugins(plugins):
    """Loads the plugins defined in the plugins list."""
    for plugin_file in plugins:
        plugin = import_module(plugin_file)
        plugin.register()
