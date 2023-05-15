import numpy as np
import matplotlib.pyplot as plt

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
ax.annotate('$x$', xy=(1, 0), xycoords=('axes fraction', 'data'), 
            xytext=(arrow_length, 0), textcoords='offset points',
            ha='left', va='center',
            arrowprops=dict(arrowstyle='<|-', fc='black'))

#-- Y-axis arrow
ax.annotate('$A$', xy=(0, 1), xycoords=('data', 'axes fraction'), 
            xytext=(0, arrow_length), textcoords='offset points',
            ha='center', va='bottom',
            arrowprops=dict(arrowstyle='<|-', fc='black'))

#-- Plot
ax.axis([-5.25*np.pi/2, 7.6*np.pi, -7.2, +7.2])
ax.grid(False)
ax.set_aspect(1)


# Turn off ticks
ax.set_yticks([])
ax.set_xticks([])

# Turn off tick labels
ax.set_yticklabels([])
ax.set_xticklabels([])

#-- Function

Theta = np.linspace(-5.25*np.pi/2, 7.6*np.pi, 200)
Amplitude = 7*np.sin(Theta)
ax.plot(Theta, Amplitude, 'k-', linewidth=1)

Theta2 = np.linspace(2*np.pi, 4*np.pi-(np.pi/49), 49)
Amplitude2 = 7*np.sin(Theta2)
ax.plot(Theta2, Amplitude2, 'k-', linewidth=3)

#ax.plot(Theta2, np.zeros(40), 'ko', markersize=2)

plt.savefig("plot.png", bbox_inches='tight')

plt.show()
