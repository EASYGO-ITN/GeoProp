import reaktoro as rkt
import CoolProp as cp
import numpy as np
import matplotlib.pyplot as plt

# specific volume of pure water as a function of temperature for different EOS and activity models
samples = 200
p = 32e5

water = cp.AbstractState("?", "water")
water.update(cp.PQ_INPUTS, p, 0)
tsat = water.T()
print("Tsat;"+str(tsat))
ts = np.linspace(445, 465, samples)

cp_state = cp.AbstractState("?", "water")
cp_svol = np.zeros(samples)

db = rkt.SupcrtDatabase('supcrtbl')
aqueous = rkt.AqueousPhase("H2O(aq)")

ideal_gaseous = rkt.GaseousPhase("H2O(g)")
ideal_system = rkt.ChemicalSystem(db, aqueous, ideal_gaseous)
ideal_state = rkt.ChemicalState(ideal_system)
ideal_state.set('H2O(aq)', 1, 'kg')
ideal_state.pressure(p, "Pa")
rkt_ideal_svol = np.zeros(samples)

SRK_gaseous = rkt.GaseousPhase("H2O(g)")
SRK_gaseous.set(rkt.ActivityModelSoaveRedlichKwong())
SRK_system = rkt.ChemicalSystem(db, aqueous, SRK_gaseous)
SRK_state = rkt.ChemicalState(SRK_system)
SRK_state.set('H2O(aq)', 1, 'kg')
SRK_state.pressure(p, "Pa")
rkt_SRK_svol = np.zeros(samples)

for i, t in enumerate(ts):

    def get_svolume(state, t):
        state.temperature(t, "K")

        res = rkt.equilibrate(state)
        props = rkt.ChemicalProps(state)
        phases = state.system().phases().size()
        masses = np.array([props.phaseProps(i).mass()[0] for i in range(phases)])
        volumes = np.array([props.phaseProps(i).volume()[0] for i in range(phases)])

        _total_mass = sum(masses)
        _total_volume = sum(volumes)

        return _total_volume/_total_mass

    rkt_ideal_svol[i] = get_svolume(ideal_state, t)
    rkt_SRK_svol[i] = get_svolume(SRK_state, t)

    cp_state.update(cp.PT_INPUTS, p, t)
    cp_svol[i] = 1/ cp_state.rhomass()

p_str = "P0;"+ str(p) + ";"
ts_str = "Ts;"
cp_rho_str = "cp_svol;"
rkt_ideal_rho_str = "rkt_ideal_svol;"
rkt_SRK_rho_str = "rkt_SRK_svol;"
for i in range(len(ts)):
    ts_str += str(ts[i]) + ";"
    cp_rho_str += str(cp_svol[i]) + ";"
    rkt_ideal_rho_str += str(rkt_ideal_svol[i]) + ";"
    rkt_SRK_rho_str += str(rkt_SRK_svol[i]) + ";"

print(p_str)
print(ts_str)
print(cp_rho_str)
print(rkt_ideal_rho_str)
print(rkt_SRK_rho_str)

plt.plot(ts, cp_svol, label="WagnerPruß")
plt.plot(ts, rkt_ideal_svol, label="IdealGas")
plt.plot(ts, rkt_SRK_svol, label="SRK")
plt.xlabel("Temperature, K")
plt.ylabel("Specific Volume, m3/kg")

plt.legend()
plt.show()







