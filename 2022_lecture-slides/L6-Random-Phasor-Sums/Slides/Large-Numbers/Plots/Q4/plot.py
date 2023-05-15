import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss

xp = np.linspace(0, 4, 250)

RayleighPDF= ss.rayleigh.pdf(xp, 0 , 1.0)

plt.plot(xp, RayleighPDF, 'k-', lw=3)

plt.xlabel('$a/\sigma_A$',fontsize=16)
plt.ylabel('$\sigma_A\:f_A(a/\sigma_A)$',fontsize=16)

plt.savefig('plot-R.png', dpi=600, bbox_inches='tight')
plt.show()
