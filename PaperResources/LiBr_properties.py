from GeoProp.Model.Fluid import Fluid
from GeoProp.Model.Databases import Comp
from GeoProp.Model.PartitionModel import Partition
from GeoProp.Model.PropertyModel import PropertyModel

import numpy as np
from CoolProp.CoolProp import PropsSI
import matplotlib.pyplot as plt

# initialise the calculation parameters
n = 5
p = 101325
ts = np.linspace(298, 370, n)

# initialise the data stores
gp_density = np.zeros(n)
libr_density = np.zeros(n)
wp_density = np.zeros(n)

gp_enthalpy = np.zeros(n)
libr_enthalpy = np.zeros(n)
wp_enthalpy = np.zeros(n)

gp_entropy = np.zeros(n)
libr_entropy = np.zeros(n)
wp_entropy = np.zeros(n)

# data from ASPEN simulation
aspen_ts = [25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 100]
aspen_density = [1125.94191, 1124.35276, 1122.51314, 1120.44341, 1118.16008, 1115.67688, 1113.00554, 1110.15629, 1107.13826,
             1103.95957, 1100.62747, 1097.14837, 1093.52784, 1089.7707, 1081.86218]
aspen_enthalpy = [0, 16.870996, 33.7471869, 50.6325655, 67.5302083, 84.4425636, 101.371684, 118.319424, 135.287595, 152.278095,
           169.292982, 186.334529, 203.405242, 220.507877, 254.81391]
aspen_entropy = [0, 0.0561163429, 0.111331637, 0.165687748, 0.219221647, 0.271966617, 0.323953191, 0.37520991, 0.425763926,
           0.475641433, 0.524867962, 0.573468556, 0.621467867, 0.668890203, 0.762229299]

# initialise the composition
sal = 0.2
comp = [Comp.WATER, Comp.Li, Comp.Br]
alpha = (Comp.Br.value.Mr / Comp.Li.value.Mr)

mass = [1, sal / (1 + alpha), alpha * sal / (1 + alpha)]

brine = Fluid(components=comp, composition=mass)

# initialise the calculators
partition = Partition()
brine = partition.calc(brine, 101325, 298)
property = PropertyModel()

# calculate properties
for i, t in enumerate(ts):
    props = property.calc(brine, p, t)

    gp_density[i] = props.total.props.rho
    libr_density[i] = PropsSI("D", "T", t, "P", p, "INCOMP::LiBr[{}]".format(sal))
    wp_density[i] = PropsSI("D", "T", t, "P", p, "Water")

    gp_enthalpy[i] = props.total.props.h
    libr_enthalpy[i] = PropsSI("H", "T", t, "P", p, "INCOMP::LiBr[{}]".format(sal)) / 1000
    wp_enthalpy[i] = PropsSI("H", "T", t, "P", p, "Water") / 1000

    gp_entropy[i] = props.total.props.s
    libr_entropy[i] = PropsSI("S", "T", t, "P", p, "INCOMP::LiBr[{}]".format(sal)) / 1000
    wp_entropy[i] = PropsSI("S", "T", t, "P", p, "Water") / 1000

ts = ts - 273.15

# processing results
gp_enthalpy = gp_enthalpy - gp_enthalpy[0]
libr_enthalpy = libr_enthalpy - libr_enthalpy[0]
wp_enthalpy = wp_enthalpy - wp_enthalpy[0]
diff_enthalpy = (gp_enthalpy - libr_enthalpy) / (libr_enthalpy + 1e-6) * 100

gp_entropy = gp_entropy - gp_entropy[0]
libr_entropy = libr_entropy - libr_entropy[0]
wp_entropy = wp_entropy - wp_entropy[0]
diff_entropy = (gp_entropy - libr_entropy) / (libr_entropy + 1e-6) * 100

# reporting of results
print("___LIBR___;")
print("T;"+";".join([str(x) for x in ts]))
print("Density;"+";".join([str(x) for x in libr_density]))
print("Enthalpy;"+";".join([str(x) for x in libr_enthalpy]))
print("Entropy;"+";".join([str(x) for x in libr_entropy]))

print("___GEOPROP___;")
print("T;"+";".join([str(x) for x in ts]))
print("Density;"+";".join([str(x) for x in gp_density]))
print("Enthalpy;"+";".join([str(x) for x in gp_enthalpy]))
print("Entropy;"+";".join([str(x) for x in gp_entropy]))

print("___WP EOS___;")
print("T;"+";".join([str(x) for x in ts]))
print("Density;"+";".join([str(x) for x in wp_density]))
print("Enthalpy;"+";".join([str(x) for x in wp_enthalpy]))
print("Entropy;"+";".join([str(x) for x in wp_entropy]))

print("___ASPEN___;")
print("T;"+";".join([str(x) for x in aspen_ts]))
print("Density;"+";".join([str(x) for x in aspen_density]))
print("Enthalpy;"+";".join([str(x) for x in aspen_enthalpy]))
print("Entropy;"+";".join([str(x) for x in aspen_entropy]))

# plotting results

fig, axs = plt.subplots(1,3)

ax1 = axs[0]
ax1.set_title("Brine Density for {:} kg/kg LiBr".format(sal))
ax1.plot(ts, libr_density, "*", label="libr")
ax1.plot(ts, gp_density, label="GeoProp")
ax1.plot(ts, wp_density, label="WagnerPruß")
ax1.plot(aspen_ts, aspen_density, label="Aspen Plus V11")
ax1.set_xlabel("Temperature, degC")
ax1.set_ylabel("Density, kg/m3")
ax1.legend()

ax1 = axs[1]
ax1.set_title("Brine Enthalpy for {:} kg/kg LiBr".format(sal))
ax1.plot(ts, libr_enthalpy, "*", label="libr")
ax1.plot(ts, gp_enthalpy, label="GeoProp")
ax1.plot(ts, wp_enthalpy, label="WagnerPruß")
ax1.plot(aspen_ts, aspen_enthalpy, label="Aspen Plus V11")
ax1.set_xlabel("Temperature, degC")
ax1.set_ylabel("Enthalpy, kJ/kg")
ax1.legend()

ax1 = axs[2]
ax1.set_title("Brine Entropy for {:} kg/kg LiBr".format(sal))
ax1.plot(ts, libr_entropy, "*", label="libr")
ax1.plot(ts, gp_entropy, label="GeoProp")
ax1.plot(ts, wp_entropy, label="WagnerPruß")
ax1.plot(aspen_ts, aspen_entropy, label="Aspen Plus V11")
ax1.set_xlabel("Temperature, degC")
ax1.set_ylabel("Entropy, kJ/kg/K")
ax1.legend()

plt.tight_layout()
plt.show()


