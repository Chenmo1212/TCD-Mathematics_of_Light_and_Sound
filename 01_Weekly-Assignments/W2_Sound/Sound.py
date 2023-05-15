# ===========================
# @Time    : 2022/09/29 12:12
# @Author  : Long Pan
# @Id      : 21332147
# @File    : Sound.py
# ===========================


"""
https://en.wikipedia.org/wiki/Harmonic_oscillator#Damped_harmonic_oscillator
Based on the balance of forces (Newton's second law) for damped harmonic oscillators,
when damping ratio zeta(ζ) equal 0, the motion of the harmonic oscillator is undamped.

So I can use the scipy integral function named odeint to solve differential equations of
both undamped and damped Harmonic_Oscillator system

And the value of the damping ratio zeta(ζ) critically determines the behavior of the system.
A damped harmonic oscillator can be:
1. Overdamped (ζ > 1)
2. Critically damped (ζ = 1)
3. Underdamped (ζ < 1)
"""

import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np
# Solve a system of ordinary differential equations:
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.odeint.html
from scipy.integrate import odeint


def dy(y, t, zeta, w0):
    """
    First order differential equations of Harmonic_Oscillator system
    :param y: Set original differential equation and first-order differential equations
    :param t: Independent variable of original differential equation
    :param zeta: Damping ratio
    :param w0: Undamped angular frequency of the oscillator
    :return: The first-order and Second-order differential equations
    """
    # Set original differential equation and first-order differential equations
    x_0, x_1 = y

    # Set the first-order differential equation
    dx_1 = x_1
    # Set the second-order differential equation
    dx_2 = -2 * zeta * w0 * dx_1 - w0 ** 2 * x_0

    return [dx_1, dx_2]


if __name__ == '__main__':
    rcParams['figure.figsize'] = 12, 9

    t = np.linspace(0, 6, 600)
    w0 = 2 * np.pi  # w^2 = k / m

    # Set the initialization conditions of the original differential equation and the first order differential equation
    y0 = [1, 0]

    y1 = odeint(dy, y0, t, args=(0.0, w0))  # undamped           ζ = 0
    y2 = odeint(dy, y0, t, args=(0.2, w0))  # under damped       ζ < 1
    y3 = odeint(dy, y0, t, args=(1.0, w0))  # critial damping    ζ = 1
    y4 = odeint(dy, y0, t, args=(4.0, w0))  # over damped        ζ > 1

    plt.plot(t, y1[:, 0], 'k', label="Undamped(ζ = 0)")
    plt.plot(t, y2[:, 0], 'r', label="Underdamped(ζ = 0.2)")
    plt.plot(t, y3[:, 0], 'b', label=r"Critically damped(ζ = 1.0)")
    plt.plot(t, y4[:, 0], 'g', label="Overdamped(ζ = 4.0)")

    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('Motion plot of harmonic oscillator with different damping ratio')
    plt.legend(loc=1)
    plt.savefig('Sound')
    plt.show()
