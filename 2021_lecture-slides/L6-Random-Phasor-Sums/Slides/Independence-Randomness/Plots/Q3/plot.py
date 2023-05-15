import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss

x = np.linspace(-5, 5, 500)

UniformPDF = ss.uniform.pdf(x,-5,+10)
NormalPDF = ss.norm.pdf(x, 0, 1) 

plt.plot(x, UniformPDF, 'k-', label='Uniform $f_X(x), [-5,+5].$',lw=3)
plt.plot(x, NormalPDF, 'k:', label='Normal $f_X(x), [0, 1].$', lw=3)

plt.xlabel('$x$',fontsize=16)
plt.ylabel('$\mathbf{P}(x)$',fontsize=16)

plt.legend(loc='center right', fontsize=13)
plt.savefig('plot-UN.png', dpi=600, bbox_inches='tight')
plt.show()

xp = np.linspace(0, 5, 250)

ExponentialPDF = ss.expon.pdf(xp, 0, 1)
RayleighPDF= ss.rayleigh.pdf(xp, 0, 1)

plt.plot(xp, ExponentialPDF, 'k-', label='Exponential $f_X(x), [0, 1].$',lw=3)
plt.plot(xp, RayleighPDF, 'k:', label='Rayleigh $f_X(x), [0, 1].$',lw=3)

plt.xlabel('$x$',fontsize=16)
plt.ylabel('$\mathbf{P}(x)$',fontsize=16)

plt.legend(loc='center right',fontsize=13)
plt.savefig('plot-ER.png', dpi=600, bbox_inches='tight')
plt.show()
