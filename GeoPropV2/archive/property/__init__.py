import json
import os.path

# TODO implement viscosity & thermal conductivity

from .. import Pref, Tref

from . import factory
from . import loader

with open(os.path.dirname(__file__)+"\\plugins.json") as file:
    data = json.load(file)

     # load the plugins
    loader.load_plugins(data["plugins"])

    # create the property engines
    engines = {item["type"]: factory.create(item) for item in data["engines"]}


