from .Utilities import RootFinder
from .Databases import Comp
from .Fluid import Fluid
from .ErrorHandling import CalculationError

import CoolProp as cp
import math
from operator import itemgetter


class SpycherPruss2009:
    """
        The SpycherPruss2009 class contains the Spycher Pruss 2009 model for the mutual solubilities of H2O and CO2

        Attributes
        ----------
        Tmin_low: float
            the minimum allowable temperature for the low temperature model
        Tmax_low: float
            the maximum allowable temperature for the low temperature model
        Tmin_high: float
            the minimum allowable temperature for the high temperature model
        Tmax_high: float
            the maximum allowable temperature for the high temperature model
        Pmin: float
            the minimum allowable pressure
        Pmax: float
            the maximum allowable pressure

        References
        ----------
        DOI: 10.1007/s11242-009-9425-y
    """

    Tmin_low = 12 + 273.15  # degK
    Tmax_low = 99 + 273.15  # degK
    Tmin_high = 109 + 273.15  # degK
    Tmax_high = 300 + 273.15  # degK

    Pmin = 1e5
    Pmax = 600e5

    R = 83.144598  # bar.cm3/(mol.K)

    @staticmethod
    def interpolate(func, low, high, val, *args, **kwargs):
        """
            interpolates the given function between the specified bounds

            Parameters
            ----------
            func:
                the target function/method to be interpolated
            low: float
                the x value representing the lower bound
            high: float
                the x value respresenting the upper bound
            val: float
                the value x to be interpolated
            *args
                the function's positional arguments
            **kwargs
                the function's keyword arguments

            Returns
            -------
            props: float

            Raises:
            ValueError
                if the function's output type is not supported
            ValueError
                if the specificed value is outside the min-max bound
        """

        if low <= val <= high:
            val_low = func(low, *args, **kwargs)
            val_high = func(high, *args, **kwargs)
            ratio = (high - val) / (high - low)

            if type(val_low) in (int, float):
                return val_low * ratio + (1 - ratio) * val_high
            elif type(val_low) in (tuple, list, set):
                return (val_low[i] * ratio + (1 - ratio) * val_high[i] for i in range(len(val_low)))
            else:
                raise ValueError("The type of the function output is not supported ")
        else:
            raise ValueError("The value ({}) is outside the specified range (min: {} to max: {}".format(val, low, high))

    def a_CO2(self, T):
        """
            calculates the SRK "a" parameter for pure CO2

            Parameters
            ----------
            T: float
                the temperature

            Returns
            -------
            float
        """

        if self.Tmin_low <= T <= self.Tmax_low:
            # low temperature model
            return 7.54e7 - 4.13e4 * T
        elif T < self.Tmin_high:
            return self.interpolate(self.a_CO2, self.Tmax_low, self.Tmin_high, T)
        else:
            # high temperature model
            return 8.008e7 - 4.984e4 * T

    def a_H2O(self, T):
        """
            calculates the SRK "a" parameter for pure H2O

            Parameters
            ----------
            T: float
                the temperature

            Returns
            -------
            float
        """

        if self.Tmin_low <= T <= self.Tmax_low:
            # low temperature model
            return 128475900.0  # This used to be zero but ended up causing huge interpolation errors...
        elif T < self.Tmin_high:
            return self.interpolate(self.a_H2O, self.Tmax_low, self.Tmin_high, T)
        else:
            # high temperature model
            return 1.337e8 - 1.4e4 * T

    def a_CO2_H2O(self, T, aCO2_aH2O, yCO2, yH2O):
        """
            calculates the SRK "a" parameter for CO2 - H2O pairs

            Parameters
            ----------
            T: float
                the temperature
            aCO2_aH2O: float
                the product of aCO2 and aH2O
            yCO2: float
                the gas phase mole fraction of CO2
            yH2O: float
                the gas phase mole fraction of H2O

            Returns
            -------
            float, float
        """

        if self.Tmin_low <= T <= self.Tmax_low:
            # low temperature model
            return 7.89e7, 7.89e7
        elif T < self.Tmin_high:
            return self.interpolate(self.a_CO2_H2O, self.Tmax_low, self.Tmin_high, T, aCO2_aH2O, yCO2, yH2O)
        else:
            # high temperature model
            KCO2_H2O = self.K_CO2_H2O(T)
            KH2O_CO2 = self.K_H2O_CO2(T)

            kCO2_H2O = KCO2_H2O * yCO2 + KH2O_CO2 * yH2O
            kH2O_CO2 = KH2O_CO2 * yH2O + KCO2_H2O * yCO2

            aCO2_H2O = math.sqrt(aCO2_aH2O) * (1 - kCO2_H2O)
            aH2O_CO2 = math.sqrt(aCO2_aH2O) * (1 - kH2O_CO2)

            return aCO2_H2O, aH2O_CO2

    def K_CO2_H2O(self, T):
        """
            calculates the BICs for a CO2 - H2O interaction

            Parameters
            ----------
            T: float
                the temperature

            Returns
            -------
            float
        """

        if self.Tmin_low <= T <= self.Tmax_low:
            # low temperature model
            return 0.0
        elif T < self.Tmin_high:
            return self.interpolate(self.K_CO2_H2O, self.Tmax_low, self.Tmin_high, T)
        else:
            # high temperature model
            return 0.4228 - 7.422e-4 * T

    def K_H2O_CO2(self, T):
        """
            calculates the BICs for a H2O - CO2 interaction

            Parameters
            ----------
            T: float
                the temperature

            Returns
            -------
            float
        """

        if self.Tmin_low <= T <= self.Tmax_low:
            # low temperature model
            return 0.0
        elif T < self.Tmin_high:
            return self.interpolate(self.K_H2O_CO2, self.Tmax_low, self.Tmin_high, T)
        else:
            # high temperature model
            return 1.427e-2 - 4.037e-4 * T

    def a_mix(self, aCO2, aH2O, aCO2_H2O, aH2O_CO2, yCO2, yH2O):
        """
            calculates the SRK "a" parameter of the mixture

            Parameters
            ----------
            aCO2: float
                the SRK "a" parameter of pure CO2
            aH2O: float
                the SRK "a" parameter of pure H2O
            aCO2_H2O: float
                the SRK "a" parameter for a CO2 - H2O interaction pair
            aH2O_CO2: float
                the SRK "a" parameter for a H2O - CO2 interaction pair
            yCO2: float
                the gas phase mole fraction of CO2
            yH2O: float
                the gas phase mole fraction of H2O

            Returns
            -------
            float
        """

        return aCO2 * yCO2 * yCO2 + aH2O * yH2O * yH2O + (aCO2_H2O + aH2O_CO2) * yCO2 * yH2O

    def a(self, T, yCO2, yH2O):
        """
            calculates the various SRK "a" parameters for the fuid

            Parameters
            ----------
            T: float
                the temperature
            yCO2: float
                the gas phase mole fraction of CO2
            yH2O: float
                the gas phase mole fraction of H2O

            Returns
            -------
            float, float, float, float, float
        """

        aCO2 = self.a_CO2(T)
        aH2O = self.a_H2O(T)
        aCO2_H2O, aH2O_CO2 = self.a_CO2_H2O(T, aCO2 * aH2O, yCO2, yH2O)
        amix = self.a_mix(aCO2, aH2O, aCO2_H2O, aH2O_CO2, yCO2, yH2O)

        return amix, aCO2, aH2O, aCO2_H2O, aH2O_CO2

    def b_CO2(self, T):
        """
            calculates the SRK "b" parameter for pure CO2

            Parameters
            ----------
            T: float
                the temperature

            Returns
            -------
            float
        """

        if self.Tmin_low <= T <= self.Tmax_low:
            # low temperature
            return 27.8
        elif T < self.Tmin_high:
            return self.interpolate(self.b_CO2, self.Tmax_low, self.Tmin_high, T)
        else:
            # high temperature model
            return 28.25

    def b_H2O(self, T):
        """
            calculates the SRK "b" parameter for pure H2O

            Parameters
            ----------
            T: float
                the temperature

            Returns
            -------
            float
        """
        if self.Tmin_low <= T <= self.Tmax_low:
            # low temperature model
            return 18.18
        elif T < self.Tmin_high:
            return self.interpolate(self.b_H2O, self.Tmax_low, self.Tmin_high, T)
        else:
            # high temperature model
            return 15.70

    def b_mix(self, bCO2, bH2O, yCO2, yH2O):
        """
            calculates the SRK "b" parameter for the mixture

            Parameters
            ----------
            bCO2: float
                the SRK "b" parameter for pure CO2
            bH2O: float
                the SRK "b" parameter for pure H2O
            yCO2: float
                the gas phase mole fraction of CO2
            yH2O: float
                the gas phase mole fraction of H2O

            Returns
            -------
            float
        """
        return bCO2 * yCO2 + bH2O * yH2O

    def b(self, T, yCO2, yH2O):
        """
            calculates the various SRK "b" parameters for the fluid

            Parameters
            ----------
            T: float
                the temperature
            yCO2: float
                the gas phase mole fraction of CO2
            yH2O: float
                the gas phase mole fraction of H2O

            Returns
            -------
            float
        """
        bCO2 = self.b_CO2(T)
        bH2O = self.b_H2O(T)

        bmix = self.b_mix(bCO2, bH2O, yCO2, yH2O)

        return bmix, bCO2, bH2O

    def fugacity_coefficients(self, T, P, yCO2, yH2O):
        """
        calculates the fugacity coefficients of CO2 and H2O

        Parameters
        ----------
        T: float
            the temperature
        P: float
            the pressure
        yCO2: float
            the gas phase mole fraction of CO2
        yH2O:float
            the gas phase mole fraction of H2O

        Returns
        -------
        float, float

        """

        Pbar = P * 1e-5

        amix, aCO2, aH2O, aCO2_H2O, aH2O_CO2 = self.a(T, yCO2, yH2O)
        bmix, bCO2, bH2O = self.b(T, yCO2, yH2O)
        KCO2_H2O = self.K_CO2_H2O(T)
        KH2O_CO2 = self.K_H2O_CO2(T)

        a2 = -self.R * T / Pbar
        a1 = -(self.R * T * bmix/Pbar - amix/(Pbar * math.sqrt(T)) + bmix * bmix)
        a0 = -amix * bmix / (Pbar * math.sqrt(T))

        Vs = RootFinder.CubicSolver(a2, a1, a0)

        V = max(Vs)

        T05 = math.sqrt(T)
        T15 = T05 * T

        aux1 = (Pbar*V/(self.R*T)-1)/bmix
        aux2 = -math.log(Pbar*(V-bmix)/(self.R*T))
        aux3 = -(yH2O*yH2O*yCO2*(KH2O_CO2-KCO2_H2O) + yCO2*yCO2*yH2O*(KCO2_H2O-KH2O_CO2))*math.sqrt(aH2O*aCO2)
        aux4 = (amix/(bmix*self.R*T15))*math.log(V/(V+bmix))

        test = V/(V+bmix)

        c1 = (yH2O*(aH2O_CO2+aCO2_H2O)+2*yCO2*aCO2)
        c2 = yCO2*yH2O*(KCO2_H2O-KH2O_CO2)*math.sqrt(aCO2*aH2O)
        c3 = ((c1 + aux3 + c2)/amix - bCO2/bmix)

        ln_phi_CO2 = bCO2*aux1 + aux2 + c3*aux4

        h1 = (yCO2*(aCO2_H2O+aH2O_CO2)+2*yH2O*aH2O)
        h2 = yH2O*yCO2*(KH2O_CO2 - KCO2_H2O)*math.sqrt(aH2O*aCO2)
        h3 = ((h1 + aux3 + h2)/amix - bH2O/bmix)

        ln_phi_H2O = bH2O*aux1 + aux2 + h3*aux4

        return math.exp(ln_phi_CO2), math.exp(ln_phi_H2O)

    def log_K0_H2O(self, T):
        """
        calculates the log10 of the equilibrium constant of H2O at reference conditions

        Parameters
        ----------
        T: float
            the temperature

        Returns
        -------
        float

        """
        Tc = T - 273.15

        if self.Tmin_low <= T <= self.Tmax_low:
            # low temperature model
            return -2.209 + 3.097e-2 * Tc - 1.098e-4 * Tc * Tc + 2.048e-7 * Tc * Tc * Tc
        elif T < self.Tmin_high:
            return self.interpolate(self.log_K0_H2O, self.Tmax_low, self.Tmin_high, T)
        else:
            # high temperature model
            return -2.1077 + 2.8127e-2 * Tc - 8.4298e-5 * Tc * Tc + 1.4969e-7 * Tc * Tc * Tc - 1.1812e-10 * Tc * Tc * Tc * Tc

    def K0_H2O(self, T):
        """
        calculates the equilibrium constant of H2O at reference conditions

        Parameters
        ----------
        T: float
            the temperature

        Returns
        -------
        flaot

        """

        # return math.exp(log_K0_H2O(T))
        return math.pow(10, self.log_K0_H2O(T))

    def log_K0_CO2(self, T):
        """
        calculates the log10 of the equilibrium constant of CO2 at reference conditions

        Parameters
        ----------
        T: float
            the temperature

        Returns
        -------
        float

        """

        Tc = T - 273.15

        if self.Tmin_low <= T <= self.Tmax_low:
            # low temperature model
            return 1.189 + 1.304e-2 * Tc - 5.446e-5 * Tc * Tc
        elif T < self.Tmin_high:
            return self.interpolate(self.log_K0_CO2, self.Tmax_low, self.Tmin_high, T)
        else:
            # high temperature model
            return 1.668 + 3.992e-3 * Tc - 1.156e-5 * Tc * Tc + 1.593e-9 * Tc * Tc * Tc

    def K0_CO2(self, T):
        """
        calculates the equilibrium constant of H2O at reference conditions

        Parameters
        ----------
        T: float
            the temperature

        Returns
        -------
        flaot

        """

        # return math.exp(log_K0_CO2(T))
        return math.pow(10, self.log_K0_CO2(T))

    def V_CO2(self, T):
        """
        calculates the average volume of CO2

        Parameters
        ----------
        T: float
            the temperature

        Returns
        -------
        float

        """
        dT = T - 373.15
        if self.Tmin_low <= T <= self.Tmax_low:
            # low temperature
            return 32.6
        elif T < self.Tmin_high:
            return self.interpolate(self.V_CO2, self.Tmax_low, self.Tmin_high, T)
        else:
            return 32.6 + 3.413e-2 * dT

    def V_H2O(self, T):
        """
        calculates the average volume of H2O

        Parameters
        ----------
        T: float
            the temperature

        Returns
        -------
        float

        """
        dT = T - 373.15
        if self.Tmin_low <= T <= self.Tmax_low:
            # low temperature model
            return 18.1
        elif T < self.Tmin_high:
            return self.interpolate(self.V_H2O, self.Tmax_low, self.Tmin_high, T)
        else:
            # high temperature model
            return 18.1 + 3.137e-2 * dT

    def Pref_CO2(self, T):
        """
        calculates the reference pressure for CO2

        Parameters
        ----------
        T: float
            the temperature

        Returns
        -------
        float

        """

        Tcutoff = 100 + 273.15
        Tc = T - 273.15

        if self.Tmin_low <= T <= Tcutoff:
            # low temperature model
            return 1
        elif T < self.Tmin_high:
            return self.interpolate(self.Pref_CO2, self.Tmax_low, self.Tmin_high, T)
        else:
            # high temperature model
            return -1.9906e-1 + 2.0471e-3 * Tc + 1.0152e-4 * Tc * Tc - 1.4234e-6 * Tc * Tc * Tc + 1.4168e-8 * Tc * Tc * Tc * Tc

    def Pref_H2O(self, T):
        """
        calculates the reference pressure for H2O

        Parameters
        ----------
        T: float
            the temperature

        Returns
        -------
        float

        """
        Tcutoff = 100 + 273.15

        if self.Tmin_low <= T <= Tcutoff:
            return 1.0
        elif T < self.Tmin_high:
            return self.interpolate(self.Pref_H2O, self.Tmax_low, self.Tmin_high, T)

        else:
            water = cp.AbstractState("?", "Water")
            water.update(cp.QT_INPUTS, 0.5, T)
            return water.p() * 1e-5

    def K_CO2(self, T, P):
        """
        calculates the equilibrium constant for CO2

        Parameters
        ----------
        T: float
            the temperature
        P: float
            the pressure

        Returns
        -------
        float

        """
        Pbar = P * 1e-5
        return self.K0_CO2(T) * math.exp((Pbar - self.Pref_CO2(T)) * self.V_CO2(T) / (self.R * T))

    def K_H2O(self, T, P):
        """
        calculates the equilibrium constant for H2O

        Parameters
        ----------
        T: float
            the temperature
        P: float
            the pressure

        Returns
        -------
        float

        """
        Pbar = P * 1e-5
        return self.K0_H2O(T) * math.exp((Pbar - self.Pref_H2O(T)) * self.V_H2O(T) / (self.R * T))

    def A_m(self, T):
        """
        calculates a parameter for determining the species activity

        Parameters
        ----------
        T: float
            the temperature

        Returns
        -------
        float

        """
        dT = (T - 373.15)
        if self.Tmin_low <= T <= self.Tmax_low:
            # low temperature model
            return 0
        elif T < self.Tmin_high:
            return self.interpolate(self.A_m, self.Tmax_low, self.Tmin_high, T)
        else:
            # high temperature model

            return -3.084e-2 * dT + 1.927e-5 * dT * dT

    def activity_coefficients(self, T, xCO2, xH2O):
        """
        calculates the activity coefficient of CO2 and H2O

        Parameters
        ----------
        T: float
            the temperature
        xCO2: float
            the liquid phase mole fraction of CO2
        xH2O: float
            the liquid phase mole fraction of CO2

        Returns
        -------
        float, float

        """
        Am = self.A_m(T)

        ln_gammaCO2 = 2 * Am * xCO2 * xH2O * xH2O
        ln_gammeH2O = (Am - 2 * Am * xH2O) * xCO2 * xCO2

        return math.exp(ln_gammaCO2), math.exp(ln_gammeH2O)

    def lambda_(self, T):
        """
        calculates the lambda parameter for the activity model

        Parameters
        ----------
        T: float
            the temperature

        Returns
        -------
        float

        """
        InvT = 1 / T

        return 2.217e-4 * T + 1.074 * InvT + 2648 * InvT * InvT

    def xi_(self, T):
        """
        calculates the xi parameter for the activity model

        Parameters
        ----------
        T: float
            the temperature

        Returns
        -------
        float

        """
        InvT = 1 / T

        return 1.3e-5 * T - 20.12 * InvT + 5259 * InvT * InvT

    def gamma_CO2_correction(self, T, mNa, mK, mCa, mMg, mCl, mSO4):
        """
        calculates the CO2 activity coefficient correction for the presence of minerals in the aqueous phase

        Parameters
        ----------
        T: float
            the temperature
        mNa: float
            the molality of Na+
        mK: float
            the molality of K+
        mCa: float
            the molality of Ca+2
        mMg: float
            the molality of Mg+2
        mCl: float
            the molality of Cl-
        mSO4: float
            the molality of SO4-2

        Returns
        -------
        float

        """

        lamb = self.lambda_(T)
        xi = self.xi_(T)

        aux1 = 1 + (mNa + mK + mCa + mMg + mCl + mSO4) / 55.508
        aux2 = 2 * lamb * (mNa + mK + 2 * mCa + 2 * mMg)
        aux3 = xi * mCl * (mNa + mK + mCa + mMg)

        gamma_correction = aux1 * math.exp(aux2 + aux3 - 0.07 * mSO4)

        return gamma_correction

    def calc(self, T, P, ion_molalities):
        """
        calculates the mutual solubilities of CO2 and H2O

        Parameters
        ----------
        T: float
            the temperature
        P: float
            the pressure
        ion_molalities: dict
            the molalities of ionic species

        Returns
        -------
        float, float, float

        """

        if T < self.Tmin_low:
            raise ValueError("The temperature ({} K)is below the minimum temperature ({} K)".format(T, self.Tmin_low))
        if T > self.Tmax_high:
            raise ValueError("The temperature ({} K)is above the maximum temperature ({} K)".format(T, self.Tmax_high))
        if P < self.Pmin:
            raise ValueError("The pressure ({} Pa)is below the minimum pressure ({} Pa)".format(P, self.Pmin))
        if P > self.Pmax:
            raise ValueError("The pressure ({} Pa)is above the maximum pressure ({} Pa)".format(P, self.Pmax))

        Pbar = P * 1e-5
        mNa, mK, mCa, mMg, mCl, mSO4 = itemgetter("Na", "K", "Ca", "Mg", "Cl", "SO4")(ion_molalities)

        KCO2 = self.K_CO2(T, P)
        KH2O = self.K_H2O(T, P)

        gammaCO2corr = self.gamma_CO2_correction(T, mNa, mK, mCa, mMg, mCl, mSO4)

        yH2O = 0
        xCO2 = 0
        xSalt = 0
        mSalt = mNa + mK + mCa + mMg + mCl + mSO4

        max_iter = 1

        if T > self.Tmin_high:
            yH2O = self.Pref_H2O(T) / Pbar
            xCO2 = 0.009
            max_iter = 10

        xH2O = 1 - xCO2 - xSalt
        for i in range(max_iter):
            mCO2 = xCO2 * 55.508 / xH2O
            xSalt = mSalt / (55.508 + mSalt + mCO2)

            yCO2 = 1 - yH2O
            xH2O = 1 - xCO2 - xSalt

            phiCO2, phiH2O = self.fugacity_coefficients(T, P, yCO2, yH2O)
            gammaCO2, gammaH2O = self.activity_coefficients(T, xCO2, xH2O)

            # A = KH2O * gammaH2O / (phiH2O * Pbar + 1e-6) + 1e-8 # included fudge factors to prevent division by zero
            # B = phiCO2 * Pbar / (55.508 * gammaCO2 * gammaCO2corr * KCO2 + 1e-6) + 1e-8  # included a fudge factors to prevent division by zero

            A = KH2O * gammaH2O / (phiH2O * Pbar)
            B = phiCO2 * Pbar / (55.508 * gammaCO2 * gammaCO2corr * KCO2)

            yH2O = (1 - B) * 55.508 / ((1 / A - B) * (mSalt + 55.508) + mSalt * B)
            xCO2 = B * (1 - yH2O)

        return yH2O, xCO2, xSalt


class SpycherPrussPartition:
    """
        The ReaktoroPartition class orchestrates the fluid partition using SpycherPruss2009

        References
        ----------
        DOI: 10.1007/s11242-009-9425-y
    """

    Tmin = SpycherPruss2009.Tmin_low
    Tmax = SpycherPruss2009.Tmax_high

    @staticmethod
    def calc(fluid, P, T, options):
        """
        orchestrates the partition calculation using SpycherPruss 2009

        Parameters
        ----------
        fluid: Fluid
            the fluid to be partitioned
        P: float
            the pressure
        T: float
            the temperature
        options: None
            the calculation options - dummy input, not used

        Returns
        -------
        Fluid

        """

        MrH2O = 0.018015
        MrCO2 = 0.044

        targetComps = [Comp.WATER, Comp.STEAM, Comp.Na_plus, Comp.K_plus, Comp.Ca_plus2, Comp.Mg_plus2, Comp.Cl_minus, Comp.SO4_minus2, Comp.CARBONDIOXIDE, Comp.CO3_minus2, Comp.CO2_aq]

        moles = {"H2O": 0.0, "Na": 0.0, "K": 0.0, "Ca": 0.0, "Mg": 0.0, "Cl": 0.0, "SO4": 0.0, "CO2": 0.0}
        molality = {"Na": 0.0, "K": 0.0, "Ca": 0.0, "Mg": 0.0, "Cl": 0.0, "SO4": 0.0}

        for comp in targetComps:
            if comp in fluid.total.components:
                if comp in [Comp.WATER, Comp.STEAM]:
                    moles["H2O"] += fluid.total.moles[comp]
                elif comp == Comp.Na_plus:
                    moles["Na"] += fluid.total.moles[comp]
                elif comp == Comp.K_plus:
                    moles["K"] += fluid.total.moles[comp]
                elif comp == Comp.Ca_plus2:
                    moles["Ca"] += fluid.total.moles[comp]
                elif comp == Comp.Mg_plus2:
                    moles["Mg"] += fluid.total.moles[comp]
                elif comp == Comp.Cl_minus:
                    moles["Cl"] += fluid.total.moles[comp]
                elif comp == Comp.SO4_minus2:
                    moles["SO4"] += fluid.total.moles[comp]
                elif comp in [Comp.CARBONDIOXIDE, Comp.CO3_minus2, Comp.CO2_aq]:
                    moles["CO2"] += fluid.total.moles[comp]

        for ion in molality:
            molality[ion] += moles[ion] / (moles["H2O"]*MrH2O)

        zH2O = moles["H2O"] / sum([moles[i] for i in moles])
        zCO2 = moles["CO2"] / sum([moles[i] for i in moles])

        water = cp.AbstractState("?", "Water")
        water.update(cp.QT_INPUTS, 0.5, T)
        Psat = water.p()

        if P > Psat:
            yH2O, xCO2, xsalts = SpycherPruss2009().calc(T, P, molality)

            yCO2 = 1 - yH2O
            xH2O = 1 - xCO2 - xsalts

            if yH2O <= 1:
                alpha = (zH2O - xH2O) / (yH2O - xH2O)
            else:
                alpha = None
        else:
            alpha = 1.1  # all the water has boiled off

        components = [Comp.Na_plus, Comp.K_plus, Comp.Ca_plus2, Comp.Mg_plus2, Comp.Cl_minus, Comp.SO4_minus2]
        composition = [fluid.total.mass[i] if i in fluid.total.components else 0.0 for i in components]

        mass_H2O = 0.0
        if Comp.WATER in fluid.total.components:
            mass_H2O += fluid.total.mass[Comp.WATER]

        if Comp.STEAM in fluid.total.components:
            mass_H2O += fluid.total.mass[Comp.STEAM]

        mass_CO2 = 0.0
        if Comp.CO2_aq in fluid.total.components:
            mass_CO2 += fluid.total.mass[Comp.CO2_aq]

        if Comp.CARBONDIOXIDE in fluid.total.components:
            mass_CO2 += fluid.total.mass[Comp.CARBONDIOXIDE]
        if Comp.CO3_minus2 in fluid.total.components:
            mass_CO2 += fluid.total.mass[Comp.CO3_minus2] * 44 / 60

        if alpha is None:
            # water boiled off - lets see how this works out
            components += [Comp.STEAM, Comp.CARBONDIOXIDE]
            composition += [mass_H2O, mass_CO2]
        elif alpha < 0:
            # the fluid is totally liquid
            components += [Comp.WATER, Comp.CO2_aq]
            composition += [mass_H2O, mass_CO2]
        elif alpha > 1:
            # the fluid is totally vapour
            components += [Comp.STEAM, Comp.CARBONDIOXIDE]
            composition += [mass_H2O, mass_CO2]
        else:
            # two phase mixtures
            components += [Comp.WATER, Comp.STEAM, Comp.CO2_aq, Comp.CARBONDIOXIDE]
            n_tot = sum([fluid.total.moles[i] for i in fluid.total.components])

            m_WAT = n_tot * (1 - alpha) * xH2O * MrH2O
            m_STEAM = n_tot * alpha * yH2O * MrH2O
            m_CO2aq = n_tot * (1 - alpha) * xCO2 * MrCO2
            m_CO2g = n_tot * alpha * yCO2 * MrCO2

            composition += [m_WAT, m_STEAM, m_CO2aq, m_CO2g]

        # create a new fluid
        return Fluid(components=components, composition=composition)