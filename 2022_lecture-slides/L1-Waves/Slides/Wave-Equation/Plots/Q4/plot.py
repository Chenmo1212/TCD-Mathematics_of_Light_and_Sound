# FS acoustic wave propagation plots using sum of sinusoids solution, 2017-01-17

import numpy as np
import matplotlib.pyplot as plt
import math

fig = plt.figure()
ax = plt.gca()

#-- Set axis spines at 0
for spine in ['left', 'bottom']:
    ax.spines[spine].set_position('zero')

#-- Hide the other spines...
for spine in ['right', 'top']:
    ax.spines[spine].set_color('none')

#-- Decorate the spines
arrow_length = 20 # In points

#-- X-axis arrow
ax.annotate(r'$\theta$', xy=(1, 0), xycoords=('axes fraction', 'data'), 
            xytext=(arrow_length, 0), textcoords='offset points',
            ha='left', va='center',
            arrowprops=dict(arrowstyle='<|-', fc='black'))

#-- Y-axis arrow
ax.annotate('$A$', xy=(0, 1), xycoords=('data', 'axes fraction'), 
            xytext=(0, arrow_length), textcoords='offset points',
            ha='center', va='bottom',
            arrowprops=dict(arrowstyle='<|-', fc='black'))

#-- Plot
ax.axis([-5.25*np.pi/2, 7.6*np.pi, -6, +6])
ax.grid(False)
ax.set_aspect(1)


# Turn off ticks
ax.set_yticks([])
ax.set_xticks([])

# Turn off tick labels
ax.set_yticklabels([])
ax.set_xticklabels([])

#-- Function
Theta = np.linspace(-5.25*np.pi/2, 7.6*np.pi, 300)

R = 0.33

AmplitudeBefore = 7*R*np.sin(Theta-np.pi/5)
ax.plot(Theta, AmplitudeBefore, 'k--', linewidth=1)

AmplitudeAfter = 7*(1-R)*np.sin(Theta+np.pi/5)
ax.plot(Theta, AmplitudeAfter, 'k.', markersize=1)

ax.plot(Theta, AmplitudeBefore+AmplitudeAfter, 'k-', linewidth=1.5)

plt.savefig("plot.png", dpi=600, bbox_inches='tight')

plt.show()
