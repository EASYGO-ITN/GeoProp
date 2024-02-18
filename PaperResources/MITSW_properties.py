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
mitsw_density = np.zeros(n)
wp_density = np.zeros(n)

gp_enthalpy = np.zeros(n)
mitsw_enthalpy = np.zeros(n)
wp_enthalpy = np.zeros(n)

gp_entropy = np.zeros(n)
mitsw_entropy = np.zeros(n)
wp_entropy = np.zeros(n)

# data from ASPEN simulation
aspen_ts = [25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 100]
aspen_density = [1062.66966, 1061.16982, 1059.43357, 1057.48014, 1055.32513, 1052.98147, 1050.46025, 1047.77111, 1044.92268,
             1041.92261, 1038.77776, 1035.49417, 1032.0771, 1028.53108, 1021.06698]
aspen_enthalpy = [0, 18.7635581, 37.519905, 56.2741644, 75.030399, 93.7919375, 112.561633, 131.342073, 150.135745, 168.945163,
           187.772951, 206.621899, 225.494987, 244.395405, 282.286584]
aspen_entropy = [0, 0.0624114327, 0.123778237, 0.184150544, 0.243572736, 0.30208483, 0.359723539, 0.416523103, 0.472515938,
           0.527733105, 0.58220464, 0.635959763, 0.689027, 0.741434266, 0.844525813]

# initialise the composition
sal = 0.1
comp = [Comp.WATER, Comp.Halite]
mass = [1, sal]
brine = Fluid(components=comp, composition=mass)

# initialise the calculators
partition = Partition()
brine = partition.calc(brine, 101325, 298)
property = PropertyModel()

# calculate properties
for i, t in enumerate(ts):
    props = property.calc(brine, p, t)

    gp_density[i] = props.total.props.rho
    mitsw_density[i] = PropsSI("D", "T", t, "P", p, "INCOMP::MITSW[{}]".format(sal))
    wp_density[i] = PropsSI("D", "T", t, "P", p, "Water")

    gp_enthalpy[i] = props.total.props.h
    mitsw_enthalpy[i] = PropsSI("H", "T", t, "P", p, "INCOMP::MITSW[{}]".format(sal)) / 1000
    wp_enthalpy[i] = PropsSI("H", "T", t, "P", p, "Water") / 1000

    gp_entropy[i] = props.total.props.s
    mitsw_entropy[i] = PropsSI("S", "T", t, "P", p, "INCOMP::MITSW[{}]".format(sal)) / 1000
    wp_entropy[i] = PropsSI("S", "T", t, "P", p, "Water") / 1000

ts = ts - 273.15

# processing results
gp_enthalpy = gp_enthalpy - gp_enthalpy[0]
mitsw_enthalpy = mitsw_enthalpy - mitsw_enthalpy[0]
wp_enthalpy = wp_enthalpy - wp_enthalpy[0]
diff_enthalpy = (gp_enthalpy - mitsw_enthalpy) / (mitsw_enthalpy + 1e-6) * 100

gp_entropy = gp_entropy - gp_entropy[0]
mitsw_entropy = mitsw_entropy - mitsw_entropy[0]
wp_entropy = wp_entropy - wp_entropy[0]
diff_entropy = (gp_entropy - mitsw_entropy) / (mitsw_entropy + 1e-6) * 100

# reporting of results
print("___MITSW___;")
print("T;"+";".join([str(x) for x in ts]))
print("Density;"+";".join([str(x) for x in mitsw_density]))
print("Enthalpy;"+";".join([str(x) for x in mitsw_enthalpy]))
print("Entropy;"+";".join([str(x) for x in mitsw_entropy]))

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
ax1.set_title("Brine Density for {:} kg/kg NaCl".format(sal))
ax1.plot(ts, mitsw_density, "*", label="MITSW")
ax1.plot(ts, gp_density, label="GeoProp")
ax1.plot(ts, wp_density, label="WagnerPruß")
ax1.plot(aspen_ts, aspen_density, label="Aspen Plus V11")
ax1.set_xlabel("Temperature, degC")
ax1.set_ylabel("Density, kg/m3")
ax1.legend()

ax1 = axs[1]
ax1.set_title("Brine Enthalpy for {:} kg/kg NaCl".format(sal))
ax1.plot(ts, mitsw_enthalpy, "*", label="MITSW")
ax1.plot(ts, gp_enthalpy, label="GeoProp")
ax1.plot(ts, wp_enthalpy, label="WagnerPruß")
ax1.plot(aspen_ts, aspen_enthalpy, label="Aspen Plus V11")
ax1.set_xlabel("Temperature, degC")
ax1.set_ylabel("Enthalpy, kJ/kg")
ax1.legend()

ax1 = axs[2]
ax1.set_title("Brine Entropy for {:} kg/kg NaCl".format(sal))
ax1.plot(ts, mitsw_entropy, "*", label="MITSW")
ax1.plot(ts, gp_entropy, label="GeoProp")
ax1.plot(ts, wp_entropy, label="WagnerPruß")
ax1.plot(aspen_ts, aspen_entropy, label="Aspen Plus V11")
ax1.set_xlabel("Temperature, degC")
ax1.set_ylabel("Entropy, kJ/kg/K")
ax1.legend()

plt.tight_layout()
plt.show()


