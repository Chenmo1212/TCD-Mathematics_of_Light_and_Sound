#!/usr/bin/env python
 
# import useful modules
import matplotlib.pyplot as plt 
import numpy as np
from pylab import *
from scipy.integrate import ode
  
class charge:
    def __init__(self, q, pos):
        self.q=q
        self.pos=pos
 
def E_point_charge(q, a, x, y):
    return q*(x-a[0])/((x-a[0])**2+(y-a[1])**2)**(1.5), \
        q*(y-a[1])/((x-a[0])**2+(y-a[1])**2)**(1.5)
 
def E_total(x, y, charges):
    Ex, Ey=0, 0
    for C in charges:
        E=E_point_charge(C.q, C.pos, x, y)
        Ex=Ex+E[0]
        Ey=Ey+E[1]
    return [ Ex, Ey ]
 

# charges and positions
#charges=[ charge(1, [-1, 0]), charge(-1, [1, 0]) ]
charges=[ charge(1, [-1, 0]) ]
 
# plot field lines
x0, x1=-2, 2
y0, y1=-1.5, 1.5
x=linspace(x0, x1, 64)
y=linspace(y0, y1, 64)
x, y=meshgrid(x, y)
Ex, Ey=E_total(x, y, charges)


plt.figure(figsize=(14, 8))
streamplot(x, y, Ex, Ey, density=1.0, linewidth=4, color='k')
plt.margins(0, 0)

 
# plot point charges
for C in charges:
    if C.q>0:
        plt.plot(C.pos[0], C.pos[1], 'ko', ms=8*sqrt(C.q))
    if C.q<0:
        plt.plot(C.pos[0], C.pos[1], 'bo', ms=8*sqrt(-C.q))
 

plt.savefig("plot.png", dpi=300, bbox_inches='tight')

plt.show()
