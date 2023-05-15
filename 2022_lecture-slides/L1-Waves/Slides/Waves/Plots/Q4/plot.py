import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

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
ax.annotate('$x$ or $t$', xy=(1, 0), xycoords=('axes fraction', 'data'), 
            xytext=(arrow_length, 0), textcoords='offset points',
            ha='left', va='center',
            arrowprops=dict(arrowstyle='<|-', fc='black'))

#-- Y-axis arrow
ax.annotate('$A$', xy=(0, 1), xycoords=('data', 'axes fraction'), 
            xytext=(0, arrow_length), textcoords='offset points',
            ha='center', va='bottom',
            arrowprops=dict(arrowstyle='<|-', fc='black'))

#-- Plot
ax.axis([-4*np.pi, 8*np.pi, -7.2, +7.2])
ax.grid(False)
ax.set_aspect(1)

# Turn off ticks
ax.set_yticks([])
ax.set_xticks([])

# Turn off tick labels
ax.set_yticklabels([])
ax.set_xticklabels([])

#-- Function

Theta = np.linspace(0, 4*np.pi, 100)
Amplitude2 = 7*signal.sawtooth(Theta)
ax.plot(Theta-4*np.pi, Amplitude2, 'k-', linewidth=1)

Theta = np.linspace(0-0.1, 4*np.pi-0.1, 100)
Amplitude1 = 7*signal.square(Theta)
ax.plot(Theta+4*np.pi, Amplitude1, 'k-', linewidth=1)

Theta = np.linspace(0, 2*np.pi, 32)

Amplitude3 = 7*signal.unit_impulse(32,19)
ax.plot(Theta, Amplitude3, 'k-', linewidth=1)

Amplitude4 = 7*signal.unit_impulse(32,13)
ax.plot(Theta+2*np.pi, Amplitude4, 'k-', linewidth=1)



plt.savefig("plot.png", bbox_inches='tight')

plt.show()
