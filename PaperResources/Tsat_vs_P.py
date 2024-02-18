import reaktoro as rkt
import CoolProp as cp
import numpy as np
import matplotlib.pyplot as plt

# the saturation temperature of pure water as a function of temperature
n = 7
ps = np.logspace(0, 6, n, base=2)
# ps = np.linspace(1, 20, n)

water = cp.AbstractState("?", "water")
water_Tsat = np.zeros(n)

db = rkt.SupcrtDatabase('supcrtbl')
aqueous = rkt.AqueousPhase("H2O(aq)")

ideal_gaseous = rkt.GaseousPhase("H2O(g)")
ideal_system = rkt.ChemicalSystem(db, aqueous, ideal_gaseous)
ideal_state = rkt.ChemicalState(ideal_system)
ideal_state.set('H2O(aq)', 1, 'kg')
rkt_ideal_Tsat = np.zeros(n)

SRK_gaseous = rkt.GaseousPhase("H2O(g)")
SRK_gaseous.set(rkt.ActivityModelSoaveRedlichKwong())
SRK_system = rkt.ChemicalSystem(db, aqueous, SRK_gaseous)
SRK_state = rkt.ChemicalState(SRK_system)
SRK_state.set('H2O(aq)', 1, 'kg')
rkt_SRK_Tsat = np.zeros(n)

def get_svolume(state, t):
    state.temperature(t, "K")

    res = rkt.equilibrate(state)
    props = rkt.ChemicalProps(state)
    phases = state.system().phases().size()
    masses = np.array([props.phaseProps(i).mass()[0] for i in range(phases)])
    volumes = np.array([props.phaseProps(i).volume()[0] for i in range(phases)])

    _total_mass = sum(masses)
    _total_volume = sum(volumes)

    return _total_volume / _total_mass

for i, p in enumerate(ps):
    ideal_state.pressure(p*1e5, "Pa")
    SRK_state.pressure(p*1e5, "Pa")

    water.update(cp.PQ_INPUTS, p*1e5, 0)

    t = water.T()
    vol = get_svolume(ideal_state, t)
    while vol < 0.03:  # this is the average specific volume for liquid and vapour phase
        t += 0.1
        try:
            vol = get_svolume(ideal_state, t)
        except:
            t = np.NAN
            break
    rkt_ideal_Tsat[i] = t

    t = water.T()
    vol = get_svolume(SRK_state, t)
    while vol < 0.03:  # this is the average specific volume for liquid and vapour phase
        t += 0.1
        try:
            vol = get_svolume(SRK_state, t)
        except:
            t = np.NAN
            break
    rkt_SRK_Tsat[i] = t

    water_Tsat[i] = water.T()

p_str = "P;"+ ";".join([str(x) for x in ps])
water_Tsat_str = "water_tsat;" + ";".join([str(x) for x in water_Tsat])
rkt_SRK_Tsat_str = "rkt_SRK_tsat;" + ";".join([str(x) for x in rkt_SRK_Tsat])
rkt_ideal_Tsat_str = "rkt_ideal_tsat;" + ";".join([str(x) for x in rkt_ideal_Tsat])

print(p_str)
print(water_Tsat_str)
print(rkt_SRK_Tsat_str)
print(rkt_ideal_Tsat_str)








