import CoolProp as cp
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root_scalar

Tref = 298
Pref = 101325

Tin = 200 + 273.15
xin = 0.2

samples = 51

cp_fluid = cp.AbstractState("?", "water")
cp_fluid.update(cp.PT_INPUTS, Pref, Tref)
cp_h0 = cp_fluid.hmass() / 1000
cp_s0 = cp_fluid.smass() / 1000  # convert to kJ

cp_fluid.update(cp.QT_INPUTS, xin, Tin)
cp_htot = cp_fluid.hmass() / 1000 - cp_h0
cp_stot = cp_fluid.smass() / 1000 - cp_s0

cp_fluid.update(cp.QT_INPUTS, 0, Tin)
cp_psat = cp_fluid.p()
cp_hsat = cp_fluid.hmass() / 1000 - cp_h0

cp_hs = np.linspace(0, cp_htot, samples - 1)
cp_hs = np.sort(np.append(cp_hs, cp_hsat))

cp_ts = np.zeros(samples)
cp_xs = np.zeros(samples)

for i, cp_h in enumerate(cp_hs):
    cp_fluid.update(cp.HmassP_INPUTS, (cp_h + cp_h0)*1000, cp_psat)
    cp_ts[i] = cp_fluid.T()
    cp_xs[i] = cp_fluid.Q()

# _____________________________________________________________________________________________________________________

from GeoProp.Model.Fluid import Fluid as GeoFluid
from GeoProp.Model.Databases import Comp
from GeoProp.Model.PartitionModel import PartitionModelOptions
from GeoProp.Model.State import State

components = [Comp.WATER, Comp.Halite]
composition = [0.95, 0.05]
geoprop_brine = GeoFluid(components=components, composition=composition)

part_opts = PartitionModelOptions()
part_opts.Reaktoro.gaseousActivityModel = PartitionModelOptions().Reaktoro.GaseousActivityModels.SOAVE_REDLICH_KWONG
brine_state = State(part_options=part_opts)

# brine_state = State()

brine_samples_a = 20
brine_samples_b = 40
brine_samples = brine_samples_a + brine_samples_b

geoprop_brine_ts_a = np.linspace(298, 470, brine_samples_a)
geoprop_brine_ts_b = np.linspace(470, 510, brine_samples_b)
geoprop_brine_ts = np.concatenate((geoprop_brine_ts_a, geoprop_brine_ts_b))
geoprop_brine_hs = np.zeros(brine_samples)
geoprop_brine_xs = np.zeros(brine_samples)

p = cp_psat


def h_search_p(p):
    temp_fluid = brine_state.calc_PT(geoprop_brine, p, Tin)
    # print(cp_hs[-1] - temp_fluid.total.props.h)
    return cp_hs[-1] - temp_fluid.total.props.h


solution = root_scalar(h_search_p, method="brentq", bracket=[1.4e6, 20e6])
p = solution.root

for i, t in enumerate(geoprop_brine_ts):
    try:
        temp_fluid = brine_state.calc_PT(geoprop_brine, p, t)
        geoprop_brine_hs[i] = temp_fluid.total.props.h
        geoprop_brine_xs[i] = temp_fluid.gaseous.props.m / temp_fluid.total.props.m
    except:
        geoprop_brine_hs[i] = np.NaN
        geoprop_brine_xs[i] = np.NaN

geoprop_brine_psat = p * 1.0

#  ____________________________________________________________________________________________________________________

components = [Comp.WATER, Comp.CARBONDIOXIDE]
composition = [0.95, 0.05]
geoprop_watNCG = GeoFluid(components=components, composition=composition)

part_opts = PartitionModelOptions()
part_opts.model = PartitionModelOptions.PartitionModels.SPYCHERPRUSS
watNCG_state = State(part_options=part_opts)

geoprop_watNCG_ts = np.zeros(samples)
geoprop_watNCG_xs = np.zeros(samples)

p = cp_psat


def h_search_p(p):
    temp_fluid = watNCG_state.calc_PT(geoprop_watNCG, p, Tin)
    # print(cp_hs[-1] - temp_fluid.total.props.h)
    return cp_hs[-1] - temp_fluid.total.props.h


solution = root_scalar(h_search_p, method="brentq", bracket=[1.4e6, 1.8e6])
p = solution.root

for i, h in enumerate(cp_hs):
    def h_search(t):
        temp_fluid = watNCG_state.calc_PT(geoprop_watNCG, p, t)
        geoprop_watNCG_xs[i] = temp_fluid.gaseous.props.m / temp_fluid.total.props.m

        return h - temp_fluid.total.props.h

    solution = root_scalar(h_search, method="brentq", bracket=[290, cp_ts[-1] + 30])

    geoprop_watNCG_ts[i] = solution.root

geoprop_watNCG_psat = p *1.0

# _____________________________________________________________________________________________________________________

components = [Comp.WATER, Comp.CARBONDIOXIDE, Comp.Na_plus, Comp.Cl_minus]
composition = [0.9, 0.05, 0.01967, 0.03033]
geoprop_brineNCG = GeoFluid(components=components, composition=composition)

part_opts = PartitionModelOptions()
part_opts.model = PartitionModelOptions.PartitionModels.SPYCHERPRUSS
brineNCG_state = State(part_options=part_opts)

geoprop_brineNCG_ts = np.zeros(samples)
geoprop_brineNCG_xs = np.zeros(samples)

p = cp_psat


def h_search_p(p):
    temp_fluid = brineNCG_state.calc_PT(geoprop_brineNCG, p, Tin)
    # print(cp_hs[-1] - temp_fluid.total.props.h)
    return cp_hs[-1] - temp_fluid.total.props.h


solution = root_scalar(h_search_p, method="brentq", bracket=[1.4e6, 1.8e6])
p = solution.root

for i, h in enumerate(cp_hs):

    def h_search(t):
        temp_fluid = brineNCG_state.calc_PT(geoprop_brineNCG, p, t)
        geoprop_brineNCG_xs[i] = temp_fluid.gaseous.props.m / temp_fluid.total.props.m
        return h - temp_fluid.total.props.h

    solution = root_scalar(h_search, method="brentq", bracket=[290, cp_ts[-1] + 30])

    geoprop_brineNCG_ts[i] = solution.root

geoprop_brineNCG_psat = p *1.0

# _____________________________________________________________________________________________________________________

plt.plot(cp_hs, cp_ts, label="Pure Water")
plt.plot(geoprop_brine_hs, geoprop_brine_ts, label="Brine")
plt.plot(cp_hs, geoprop_watNCG_ts, label="Water&NCG")
plt.plot(cp_hs, geoprop_brineNCG_ts, label="Brine&NCG")

plt.xlabel("Heat Content, kJ/kg")
plt.ylabel("Temperature, K")
plt.legend()
plt.show()

print("CP_H;"+";".join([str(x) for x in cp_hs]))
print("CP_T;"+";".join([str(x) for x in cp_ts]))

print("GP_WatNCG_T;"+";".join([str(x) for x in geoprop_watNCG_ts]))
print("GP_BrineNCG_T;"+";".join([str(x) for x in geoprop_brineNCG_ts]))
print("GP_Brine_T;"+";".join([str(x) for x in geoprop_brine_ts]))
print("GP_Brine_H;"+";".join([str(x) for x in geoprop_brine_hs]))

print("CP_X;"+";".join([str(x) for x in cp_xs]))
print("GP_WatNCG_X;"+";".join([str(x) for x in geoprop_watNCG_xs]))
print("GP_Brine_X;"+";".join([str(x) for x in geoprop_brine_xs]))
print("GP_BrineNCG_X;"+";".join([str(x) for x in geoprop_brineNCG_xs]))

print("CP_Psat;"+"{};".format(cp_psat))
print("GP_WatNCG_Psat;"+"{};".format(geoprop_watNCG_psat))
print("GP_Brine_Psat;"+"{};".format(geoprop_brine_psat))
print("GP_BrineNCG_Psat;"+"{};".format(geoprop_brineNCG_psat))

print("__________________________")

print(cp_hs)
print(cp_ts)
print(geoprop_watNCG_ts)
print(geoprop_brineNCG_ts)
print(geoprop_brine_ts)
print(geoprop_brine_hs)
print(cp_xs)
print(geoprop_brine_xs)
print(geoprop_watNCG_xs)
print(geoprop_brineNCG_xs)

print(cp_psat)
print(geoprop_brine_psat)
print(geoprop_watNCG_psat)
print(geoprop_brineNCG_psat)
