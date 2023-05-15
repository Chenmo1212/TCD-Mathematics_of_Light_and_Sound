import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def dipole(m, r, r0):
    """
    Calculation of field B in point r. B is created by a dipole moment m located in r0.
    """
# R = r - r0 - subtraction of elements of vectors r and r0, transposition of array
    R = np.subtract(np.transpose(r), r0).T
# Spatial components of r are the outermost axis
    norm_R = np.sqrt(np.einsum("i...,i...", R, R)) # einsum - Einsteinova sumace
# Dot product of R and m
    m_dot_R = np.tensordot(m, R, axes=1)
# Computation of B
    B = 3 * m_dot_R * R / norm_R**5 - np.tensordot(m, 1 / norm_R**3, axes=0)
    B *= 1e-7   # abbreviation for B = B * 1e-7, multiplication B of 1e-7, permeability of vacuum: 4\pi * 10^(-7)
# The result is the magnetic field B
    return B

X = np.linspace(-0.7, 0.7)
Y = np.linspace(-0.4, .4)

Bx, By = dipole(m=[0, 1], r=np.meshgrid(X, Y), r0=[-0.2,0.2])

plt.figure(figsize=(14, 8))
plt.streamplot(X, Y, Bx, By, density=1.0, linewidth=4,color='k')
plt.margins(0, 0)


plt.savefig("plot.png", dpi=300, bbox_inches='tight')

plt.show()
