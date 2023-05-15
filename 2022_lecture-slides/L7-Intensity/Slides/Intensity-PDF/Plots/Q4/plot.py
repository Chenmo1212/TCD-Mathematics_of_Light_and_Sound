import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss

xp = np.linspace(0, 4, 250)

ExponentialPDF = ss.expon.pdf(xp)

RayleighPDF= ss.rayleigh.pdf(xp, 0 , 1.0)

plt.plot(xp, ExponentialPDF, 'k-', lw=3,
         label='Intensity I: $\sigma_I\: f_I(i/\sigma_I)$')

plt.plot(xp, RayleighPDF, 'k:', lw=3,
         label ='Amplitude A: $\sigma_A\: f_A(a/\sigma_A)$')

plt.legend(loc='upper right',fontsize=16)

plt.xlabel(r'$i/\sigma_I$ and $a/\sigma_A$',fontsize=16)
#plt.ylabel('\mathbf{P}(.)', fontsize=16)

plt.savefig('plot-ER.png', dpi=600, bbox_inches='tight')
plt.show()
