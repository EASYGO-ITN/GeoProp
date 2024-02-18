from GeoProp.Model.Fluid import Fluid
from GeoProp.Model.Databases import Comp
from GeoProp.Model.PartitionModel import Partition
from GeoProp.Model.PropertyModel import PropertyModel

components = [Comp.WATER, Comp.NaCl_aq, Comp.CARBONDIOXIDE]
composition = [1, 0.1, 0.02]

brine = Fluid(components=components, composition=composition)

P = 101325  # in Pa
T = 350  # in K

brine = Partition().calc(brine, P, T)
brine = PropertyModel().calc(brine, P, T)

print(brine)
