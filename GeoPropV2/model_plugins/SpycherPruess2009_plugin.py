from math import sqrt, acos, cos, pi, log, exp, pow
from operator import itemgetter
from numpy import cbrt
import CoolProp as cp

from .BaseModel import Model
from ..model import factory
from GeoPropV2.constants import R_bar, Units
from GeoPropV2.fluid import PhaseProperties, AqueousPhase, VapourPhase, SolidPhase


def register():
    """
    Registers the Spycher Pruess 2009 partition engine

    Returns
    -------
    NoReturn
    """
    factory.register("spycher_pruess_2009", SpycherPruess2009Model)


class SpycherPruess2009:
    """
        The Spycher_Pruess_2009 class contains the Spycher Pruess 2009 model for the mutual solubilities of H2O and CO2

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

            aCO2_H2O = sqrt(aCO2_aH2O) * (1 - kCO2_H2O)
            aH2O_CO2 = sqrt(aCO2_aH2O) * (1 - kH2O_CO2)

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

        a2 = -R_bar * T / Pbar
        a1 = -(R_bar * T * bmix/Pbar - amix/(Pbar * sqrt(T)) + bmix * bmix)
        a0 = -amix * bmix / (Pbar * sqrt(T))

        Vs = cubic_solver(a2, a1, a0)

        V = max(Vs)

        T05 = sqrt(T)
        T15 = T05 * T

        aux1 = (Pbar*V/(R_bar*T)-1)/bmix
        aux2 = -log(Pbar*(V-bmix)/(R_bar*T))
        aux3 = -(yH2O*yH2O*yCO2*(KH2O_CO2-KCO2_H2O) + yCO2*yCO2*yH2O*(KCO2_H2O-KH2O_CO2))*sqrt(aH2O*aCO2)
        aux4 = (amix/(bmix*R_bar*T15))*log(V/(V+bmix))

        test = V/(V+bmix)

        c1 = (yH2O*(aH2O_CO2+aCO2_H2O)+2*yCO2*aCO2)
        c2 = yCO2*yH2O*(KCO2_H2O-KH2O_CO2)*sqrt(aCO2*aH2O)
        c3 = ((c1 + aux3 + c2)/amix - bCO2/bmix)

        ln_phi_CO2 = bCO2*aux1 + aux2 + c3*aux4

        h1 = (yCO2*(aCO2_H2O+aH2O_CO2)+2*yH2O*aH2O)
        h2 = yH2O*yCO2*(KH2O_CO2 - KCO2_H2O)*sqrt(aH2O*aCO2)
        h3 = ((h1 + aux3 + h2)/amix - bH2O/bmix)

        ln_phi_H2O = bH2O*aux1 + aux2 + h3*aux4

        return exp(ln_phi_CO2), exp(ln_phi_H2O)

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
        return pow(10, self.log_K0_H2O(T))

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
        return pow(10, self.log_K0_CO2(T))

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
        return self.K0_CO2(T) * exp((Pbar - self.Pref_CO2(T)) * self.V_CO2(T) / (R_bar * T))

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
        return self.K0_H2O(T) * exp((Pbar - self.Pref_H2O(T)) * self.V_H2O(T) / (R_bar * T))

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

        return exp(ln_gammaCO2), exp(ln_gammeH2O)

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

        gamma_correction = aux1 * exp(aux2 + aux3 - 0.07 * mSO4)

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
        mNa, mK, mCa, mMg, mCl, mSO4 = itemgetter("Na+", "K+", "Ca+2", "Mg+2", "Cl-", "SO4-2")(ion_molalities)

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


def cubic_solver(a2, a1, a0):

    p = (3 * a1 - a2 * a2) / 3
    q = (2 * a2 * a2 * a2 - 9 * a2 * a1 + 27 * a0) / 27

    R = q * q / 4 + p * p * p / 27

    if R <= 0:
        # taken from https://en.wikipedia.org/wiki/Cubic_equation#Cardano's_formula:~:text=Trigonometric%20and%20hyperbolic%20solutions
        m = 2 * sqrt(-p / 3)
        theta = acos(3 * q / (p * m)) / 3

        x1 = m * cos(theta) - a2 / 3
        x2 = m * cos(theta - 2 * pi / 3) - a2 / 3
        x3 = m * cos(theta - 4 * pi / 3) - a2 / 3
    else:
        # taken from https://mathworld.wolfram.com/CubicFormula.html#:~:text=(48)-,Defining,-(49)
        P = cbrt(-q / 2 + sqrt(R))
        Q = cbrt(-q / 2 - sqrt(R))

        x1 = P + Q - a2 / 3
        x2 = x1
        x3 = x1

    return x1, x2, x3


class SpycherPruess2009Model(Model):

    _partition = True
    _properties = False
    _properties_solid = False
    _properties_aqueous = False
    _properties_vapour = False

    _molar_masses = {"H2O": 0.01801528,
                     "CO2": 0.04401,
                     "Na+": 0.022989769,
                     "NaCl": 0.05844,
                     "Na2SO4": 0.14204,
                     "K+": 0.0390983,
                     "KCl": 0.0745513,
                     "K2SO4": 0.174259,
                     "Ca+2": 0.040078,
                     "CaCl2": 0.11098,
                     "CaSO4": 0.13614,
                     "Mg+2": 0.024305,
                     "MgCl2": 0.95211,
                     "MgSO4": 0.120366,
                     "Cl-": 0.035453,
                     "SO4-2": 0.09606}

    _component_dict = {"Water": "H2O",
                       "H2O": "H2O",
                       "H2O(g)": "H2O",
                       "H2O(aq)": "H2O",
                       "H2O(l)": "H2O",
                       "CarbonDioxide": "CO2",
                       "CO2": "CO2",
                       "CO2(g)": "CO2",
                       "CO2(aq)": "CO2",
                       "Na+": "Na+",
                       "Na(aq)": "Na+",
                       "K+": "K+",
                       "K(aq)": "K+",
                       "Ca+2": "Ca+2",
                       "Ca(aq)": "Ca+2",
                       "Mg+2": "Mg+2",
                       "Mg(aq)": "Mg+",
                       "Cl-": "Cl-",
                       "Cl(aq)": "Cl-",
                       "SO4-2": "SO4-2",
                       "SO4(aq)": "SO4-2"
                       }

    _compund_dict = {"NaCl": {"Na+": 1,
                              "Cl-": 1},
                     "Na2SO4": {"Na+": 2,
                              "SO4-2": 1},
                     "KCl": {"K+": 1,
                              "Cl-": 1},
                     "K2SO4": {"K+": 2,
                              "SO4-2": 1},
                     "CaCl2": {"Ca+2": 1,
                               "Cl-": 2},
                     "CaSO4": {"Ca+2": 1,
                               "SO4-2": 1},
                     "MgCl2": {"Mg+2": 1,
                               "Cl-": 2},
                     "MgSO4": {"Mg+2": 1,
                               "SO4-2": 1}
                     }

    def __init__(self, *args, **kwargs):

        super().__init__(args, kwargs)

        self.__initialised = False

        self._components = {"H2O": 0, "CO2": 0, "Na+": 0, "K+": 0, "Ca+2": 0, "Mg+2": 0, "Cl-": 0, "SO4-2": 0}
        self._molalities = {"Na+": 0.0, "K+": 0.0, "Ca+2": 0.0, "Mg+2": 0.0, "Cl-": 0.0, "SO4-2": 0.0}

    def init_partition(self, fluid):

        self._components = {x: 0 for x in self._components}
        self._molalities = {x: 0 for x in self._molalities}

        for i, comp in enumerate(fluid.total.components):
            if comp in self._component_dict:
                comp_name = self._component_dict[comp]
                if fluid.total.units == Units.MASS:
                    self._components[comp_name] += fluid.total.composition[i] * self._molar_masses[comp_name]
                else:
                    self._components[comp_name] += fluid.total.composition[i]
            elif comp in self._compund_dict:
                if fluid.total.units == Units.MASS:
                    for com in self._compund_dict[comp]:
                        self._components[com] += fluid.total.composition[i] * self._compund_dict[comp][com]*self._molar_masses[com]
                else:
                    for com in self._compund_dict[comp]:
                        self._components[com] += fluid.total.composition[i] * self._compund_dict[comp][com]
            else:
                comps = ", ".join([i for i in self._component_dict]+[i for i in self._compund_dict])
                msg = "The component \"{}\" is not recognised. The only permitted components for the Spycher-Pruess-2009 model are {}.".format(comp, comps)
                raise ValueError(msg)

        tot_mol = sum([self._components[i] for i in self._components])
        self._components = {comp:self._components[comp]/tot_mol for comp in self._components}

        for ion in self._molalities:
            self._molalities[ion] += self._components[ion] / (self._components["H2O"]*self._molar_masses["H2O"])

        self.__initialised = True

    def calc_partition(self, P, T, fluid):

        if not self.__initialised:

            self.init_partition(fluid)

        zH2O = self._components["H2O"] / sum([self._components[i] for i in self._components])
        zCO2 = self._components["CO2"] / sum([self._components[i] for i in self._components])

        water = cp.AbstractState("?", "Water")
        water.update(cp.QT_INPUTS, 0.5, T)
        Psat = water.p()

        if P > Psat:
            yH2O, xCO2, xsalts = SpycherPruess2009().calc(T, P, self._molalities)

            yCO2 = 1 - yH2O
            xH2O = 1 - xCO2 - xsalts

            if yH2O <= 1:
                alpha = (zH2O - xH2O) / (yH2O - xH2O)
            else:
                alpha = None
        else:
            alpha = 1.1  # all the water has boiled off

        aqu_comps = ["Na+", "K+", "Ca+2", "Mg+2", "Cl-", "SO4-2"]
        aqu_quant = [self._components[i] if i in self._components else 0.0 for i in aqu_comps]

        if alpha is None or alpha > 1:
            # water boiled off - lets see how this works out
            vap_comps = ["H2O", "CO2"]
            vap_quant = [self._components["H2O"], self._components["CO2"]]
            # tot_mol = sum(vap_quant)
            # vap_quant = [i/tot_mol for i in vap_quant]

            fluid.vapour = VapourPhase(vap_comps, vap_quant, Units.MOL)

            cations = self._components["Na+"] + self._components["K+"] + 2*self._components["Ca+2"] + 2*self._components["Mg+2"]
            anions = self._components["Cl-"] + 2*self._components["SO4-2"]

            temp_comps = [i for i in aqu_comps]
            temp_quant = [i for i in aqu_quant]
            tot_sol = sum(temp_quant)
            if tot_sol > 0:

                temp = {temp_comps[i]:temp_quant[i] for i in range(len(temp_comps))}

                sol_comps = []
                sol_quant = []

                if self._components["Cl-"] > 0:
                    nNaCl = min(temp["Na+"], temp["Cl-"])
                    if nNaCl > 0:
                        sol_comps.append("NaCl")
                        sol_quant.append(nNaCl)

                        temp["Na+"] -= nNaCl
                        temp["Cl-"] -= nNaCl

                    nKCl = min(temp["K+"], temp["Cl-"])
                    if nKCl > 0:
                        sol_comps.append("KCl")
                        sol_quant.append(nKCl)

                        temp["K+"] -= nKCl
                        temp["Cl-"] -= nKCl

                    nCaCl2 = min(temp["Ca+2"], temp["Cl-"]/2)
                    if nCaCl2 > 0:
                        sol_comps.append("CaCl2")
                        sol_quant.append(nCaCl2)

                        temp["Ca+"] -= nCaCl2
                        temp["Cl-"] -= nCaCl2*2

                    nMgCl2 = min(temp["Mg+2"], temp["Cl-"]/2)
                    if nCaCl2 > 0:
                        sol_comps.append("MgCl2")
                        sol_quant.append(nMgCl2)

                        temp["Mg+"] -= nMgCl2
                        temp["Cl-"] -= nMgCl2*2

                if self._components["SO4-2"] > 0:

                    nNa2SO4 = min(temp["Na+"]/2, temp["SO4-2"])
                    if nNa2SO4 > 0:
                        sol_comps.append("Na2SO4")
                        sol_quant.append(nNa2SO4)

                        temp["Na+"] -= nNa2SO4*2
                        temp["SO4-2"] -= nNa2SO4

                    nK2SO4 = min(temp["K+"]/2, temp["SO4-2"])
                    if nK2SO4 > 0:
                        sol_comps.append("K2SO4")
                        sol_quant.append(nK2SO4)

                        temp["K+"] -= nK2SO4*2
                        temp["SO4-2"] -= nK2SO4

                    nCaSO4 = min(temp["Ca+2"], temp["SO4-2"])
                    if nCaSO4 > 0:
                        sol_comps.append("CaSO4")
                        sol_quant.append(nCaSO4)

                        temp["Ca+2"] -= nCaSO4
                        temp["SO4-2"] -= nCaSO4

                    nMgSO4 = min(temp["Mg+2"], temp["SO4-2"])
                    if nMgSO4 > 0:
                        sol_comps.append("MgSO4")
                        sol_quant.append(nMgSO4)

                        temp["Mg+2"] -= nMgSO4
                        temp["SO4-2"] -= nMgSO4

                # tot_sol = sum(sol_quant)
                # sol_quant = [i/tot_sol if tot_sol>0 else 0 for i in sol_quant]
                fluid.solid = SolidPhase(sol_comps, sol_quant, Units)

        elif alpha < 0:
            # the fluid is totally liquid
            aqu_comps += ["H2O", "CO2"]
            aqu_quant += [self._components["H2O"], self._components["CO2"]]

            fluid.aqueous = AqueousPhase(aqu_comps, aqu_quant, Units.MOL)
        else:
            # two phase mixtures
            vap_comps = ["H2O", "CO2"]
            vap_quant = [alpha * yH2O, alpha * yCO2]
            # tot_vap = sum(vap_quant)
            # vap_quant = [i/tot_vap for i in vap_quant]

            fluid.vapour = VapourPhase(vap_comps, vap_quant, Units.MOL)

            aqu_comps += ["H2O", "CO2"]
            aqu_quant += [(1 - alpha) * xH2O, (1 - alpha) * xCO2]
            # tot_aqu = sum(aqu_quant)
            # aqu_quant = [i / tot_aqu for i in aqu_quant]

            fluid.aqueous = AqueousPhase(aqu_comps, aqu_quant, Units.MOL)
