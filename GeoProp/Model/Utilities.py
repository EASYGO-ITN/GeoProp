from .ErrorHandling import ConvergenceError
import math
import numpy as np


class RootFinder:
    """
    A class for various methods for finding the root of a function
    """

    class NewtonRaphson:
        """
        A class to find the root of a function using the Newton-Raphson method

        References:
        -----------
        TODO
        """
        def __new__(cls, func, y, x0, perturb=0.001, maxiter=25, tolerance=0.0001, others=None):
            """
            Searches for the root of a function using the Newton-Raphson method

            Parameters
            ----------
            func
                the function
            y : float
                the target value of the function
            x0 : float
                the initial guess for "x"
            perturb :float
                the perturbation of the "x" variable
            maxiter : int
                the maximum number of iterations
            tolerance : float
                the convergence tolerance
            others
                any other parameters required to execute the function
            """

            return cls.__call__(cls, func, y, x0, perturb, maxiter, tolerance, others)

        def __call__(self, func, y, x0, perturb, maxiter, tolerance, others):
            """
                        Searches for the root of a function using the Newton-Raphson method

            Parameters
            ----------
            func
                the function
            y : float
                the target value of the function
            x0 : float
                the initial guess for "x"
            perturb :float
                the perturbation of the "x" variable
            maxiter : int
                the maximum number of iterations
            tolerance : float
                the convergence tolerance
            others
                any other parameters required to execute the function

            Returns
            -------
            float
                the final "x" value

            Raises
            ------
            ConvergenceError
                if no root within the specified tolerance can be found
            """

            tolerance *= 1 + abs(y)
            perturb += 1

            result = None
            for i in range(maxiter):

                y0 = func(y, x0, others)

                x1 = x0 * perturb
                y1 = func(y, x1, others)

                # exit loop if error is below tolerance
                if abs(y0) < tolerance:
                    result = x0
                    break
                else:
                    dxdy = (x1 - x0) / (y1 - y0)
                    x0 -= y0 * dxdy

            if abs(y0) > tolerance:
                raise ConvergenceError(
                    "unable to converge on a root after {} iterations. Current error is {}".format(maxiter, y1))

            return result

    class Secant:
        """
        A class to find the root of a function using the Secant method

        References:
        -----------
        TODO
        """

        def __new__(cls, func, y, x0, x1, maxiter=25, tolerance=0.0001, others=None):
            """
            Searches for the root of a function using the Secant method

            Parameters
            ----------
            func
                the function
            y : float
                the target value of the function
            x0 : float
                the initial guess for "x"
            x1 : float
                the second guess for "x"
            maxiter : int
                the maximum number of iterations
            tolerance : float
                the convergence tolerance
            others
                any other parameters required to execute the function
            """

            return cls.__call__(cls, func, y, x0, x1, maxiter, tolerance, others)

        def __call__(self, func, y, x0, x1, maxiter, tolerance, others):
            """
            Searches for the root of a function using the Secant method

            Parameters
            ----------
            func
                the function
            y : float
                the target value of the function
            x0 : float
                the initial guess for "x"
            x1 : float
                the second guess for "x"
            maxiter : int
                the maximum number of iterations
            tolerance : float
                the convergence tolerance
            others
                any other parameters required to execute the function

            Returns
            -------
            float
                the final "x" value

            Raises
            ------
            ConvergenceError
                if the no root with the predefined tolerance can be found

            """

            tolerance *= 1 + abs(y)

            y0 = func(y, x0, others)
            y1 = y0 * 1.0

            result = None
            for i in range(maxiter):

                y1 = func(y, x1, others)

                # exit loop if error is below tolerance
                if abs(y1) < tolerance:
                    result = x1
                    break
                else:
                    x2 = x1 - y1 * (x1 - x0) / (y1 - y0)

                    x0, x1 = x1, x2
                    y0 = y1

            if abs(y1) > tolerance:
                raise ConvergenceError(
                    "unable to converge on a root after {} iterations. Current error is {}".format(maxiter, y1))

            return result

    class Brent:
        """
        Searches for the root of a function using the Brent bisection method
        """

        def __new__(cls, func, y, xa, xb, maxiter=50, tolerance=0.0001, others=None):
            """
            Searches for the root of a function using the Brent bisection method

            Parameters
            ----------
            func
                the function
            y : float
                the target value of the function
            xa : float
                the low bound for "x"
            xb : float
                the right bound for "x"
            maxiter : int
                the maximum number of iterations
            tolerance : float
                the convergence tolerance
            others
                any other parameters required to execute the function
            """

            return cls.__call__(cls, func, y, xa, xb, maxiter, tolerance, others)

        def __call__(self, func, y, xa, xb, maxiter, tolerance, others):
            """
            Searches for the root of a function using the Brent bisection method

            Parameters
            ----------
            func
                the function
            y : float
                the target value of the function
            xa : float
                the low bound for "x"
            xb : float
                the right bound for "x"
            maxiter : int
                the maximum number of iterations
            tolerance : float
                the convergence tolerance
            others
                any other parameters required to execute the function

            Returns
            -------
            float
                the final value of "x"

            Raises
            ------
            ConvergenceError
                if the solution is not initially bracketed
            ConvergenceError
                if no root can be found to the required tolerance
            """
            ya = func(y, xa, others)
            yb = func(y, xb, others)

            tolerance *= 1 + abs(y)
            # tolerance *= 1 + abs(xa - xb)

            result = None
            if ya * yb > 0:
                raise ConvergenceError(
                    "solution is not bracketed. func(xa={}) is {} and func(xb={}) is {} - they must have opposite signs".format(
                        xa, ya, xb, yb))
            else:
                if abs(ya) < abs(yb):
                    xa, xb = xb, xa
                    ya, yb = yb, ya

                xc = xa * 1.0
                xd = xa * 1.0
                yc = ya * 1.0
                xs = xb * 1.0
                ys = yb * 1.0

                flag = True
                for i in range(maxiter):
                    if yb == 0 or ys == 0 or abs(ya - yb) < tolerance:
                        result = xs
                        break
                    else:

                        if ya != yc and yb != yc:
                            p1 = xa * yb * yc / ((ya - yb) * (ya - yc))
                            p2 = xb * ya * yc / ((yb - ya) * (yb - yc))
                            p3 = xc * ya * yb / ((yc - ya) * (yc - yb))

                            xs = p1 + p2 + p3
                        else:
                            xs = xb - yb * (xb - xa) / (yb - ya)

                        cond1 = min((3 * xa + xb) / 4, xb) < xs < max((3 * xa + xb) / 4, xb)
                        cond2 = flag is True and abs(xs - xb) >= (abs(xb - xc) / 2)
                        cond3 = flag is False and abs(xs - xb) >= (abs(xc - xd) / 2)
                        cond4 = flag is True and abs(xb - xc) < tolerance
                        cond5 = flag is False and abs(xc - xd) < tolerance

                        if cond1 or cond2 or cond3 or cond4 or cond5:
                            xs = (xa + xb) / 2
                            flag = True
                        else:
                            flag = False

                        ys = func(y, xs, others)
                        xd = xc * 1.0
                        yd = yc * 1.0
                        xc = xb * 1.0
                        yc = yb * 1.0

                        if ya * ys < 0:
                            xb = xs * 1.0
                            yb = ys * 1.0
                        else:
                            xa = xs * 1.0
                            ya = ys * 1.0

                        if abs(ya) < abs(yb):
                            xa, xb = xb, xa
                            ya, yb = yb, ya

            if abs(ys) > tolerance:
                raise ConvergenceError(
                    "unable to converge on a root after {} iterations. Current error is {}".format(maxiter, yb))
            return result

    class CubicSolver:

        def __new__(cls, a2, a1, a0):

            return cls.__call__(cls, a2, a1, a0)

        def __call__(self, a2, a1, a0):

            p = (3 * a1 - a2 * a2) / 3
            q = (2 * a2 * a2 * a2 - 9 * a2 * a1 + 27 * a0) / 27

            R = q * q / 4 + p * p * p / 27

            if R <= 0:
                # taken from https://en.wikipedia.org/wiki/Cubic_equation#Cardano's_formula:~:text=Trigonometric%20and%20hyperbolic%20solutions
                m = 2 * math.sqrt(-p / 3)
                theta = math.acos(3 * q / (p * m)) / 3

                x1 = m * math.cos(theta) - a2 / 3
                x2 = m * math.cos(theta - 2 * math.pi / 3) - a2 / 3
                x3 = m * math.cos(theta - 4 * math.pi / 3) - a2 / 3
            else:
                # taken from https://mathworld.wolfram.com/CubicFormula.html#:~:text=(48)-,Defining,-(49)
                P = np.cbrt(-q / 2 + math.sqrt(R))
                Q = np.cbrt(-q / 2 - math.sqrt(R))

                x1 = P + Q - a2 / 3
                x2 = x1
                x3 = x1

            return x1, x2, x3
