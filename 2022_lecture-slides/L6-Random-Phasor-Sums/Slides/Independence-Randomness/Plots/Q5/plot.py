import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss

from numpy.random import default_rng

plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.xlabel('$x$',fontsize=16)
plt.ylabel('$y$',fontsize=16)
plt.grid(True)

rng = default_rng()

xvals = rng.standard_normal(10000)
yvals = rng.standard_normal(10000)

plt.plot(xvals, yvals, 'k.', markersize=1, label='Normal $f_{X,Y}(x,y), [0,1].$')
plt.legend(fontsize=13)

plt.savefig('plot-Scatter-Normal.png', dpi=600, bbox_inches='tight')
plt.show()

plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.xlabel('$x$',fontsize=16)
plt.ylabel('$y$',fontsize=16)
plt.grid(True)

xvals = rng.uniform(-5,+5,10000)
yvals = rng.uniform(-5,+5,10000)

plt.plot(xvals, yvals, 'k.', markersize=1, label='Uniform $f_{X,Y}(x,y), [-5,+5].$')
plt.legend(fontsize=13)

plt.savefig('plot-Scatter-Uniform.png', dpi=600, bbox_inches='tight')
plt.show()

plt.xlim(0, 5)
plt.ylim(0, 5)
plt.xlabel('$x$',fontsize=16)
plt.ylabel('$y$',fontsize=16)
plt.grid(True)

xvals = rng.exponential(1,10000)
yvals = rng.exponential(1,10000)

plt.plot(xvals, yvals, 'k.', markersize=1, label='Exponential $f_{X,Y}(x,y), [0,1].$')
plt.legend(fontsize=13)

plt.savefig('plot-Scatter-Exponential.png', dpi=600, bbox_inches='tight')
plt.show()
plt.xlim(0, 5)
plt.ylim(0, 5)
plt.xlabel('$x$',fontsize=16)
plt.ylabel('$y$',fontsize=16)
plt.grid(True)

xvals = rng.rayleigh(0.75,10000)
yvals = rng.rayleigh(0.75,10000)

plt.plot(xvals, yvals, 'k.', markersize=1, label='Rayleigh $f_{X,Y}(x,y), [0,0.75].$')
plt.legend(fontsize=13)

plt.savefig('plot-Scatter-Rayleigh.png', dpi=600, bbox_inches='tight')
plt.show()
