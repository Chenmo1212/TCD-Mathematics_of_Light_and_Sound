import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# matplotlib.rc('text', usetex=True)
# matplotlib.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]

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
ax.annotate('$t$', xy=(1, 0), xycoords=('axes fraction', 'data'), 
            xytext=(arrow_length, 0), textcoords='offset points',
            ha='left', va='center',
            arrowprops=dict(arrowstyle='<|-', fc='black'))

#-- Y-axis arrow
ax.annotate('$A$', xy=(0, 1), xycoords=('data', 'axes fraction'), 
            xytext=(0, arrow_length), textcoords='offset points',
            ha='center', va='bottom',
            arrowprops=dict(arrowstyle='<|-', fc='black'))

#-- Plot
ax.axis([-2.0*np.pi, 4.0*np.pi, -1.27, +1.27])
ax.grid(False)
ax.set_aspect(1)


# Turn off ticks
ax.set_yticks([0.625])
ax.set_xticks([])

# Turn off tick labels
ax.set_yticklabels(['1/2'])
ax.set_xticklabels([])

#-- Function

Theta = np.linspace(-2.0*np.pi, 4.0*np.pi, 200)

AmplitudeSq = 1.25*np.square(np.sin(Theta))
ax.plot(Theta, AmplitudeSq, 'k-', linewidth=1)

Amplitude = 1.25*np.sin(Theta)
ax.plot(Theta, Amplitude, 'k:', linewidth=1)

Theta2 = np.linspace(0, 4.0*np.pi, 100)
AmplitudeSqAvg = np.linspace(0.625, 0.625, 100)
ax.plot(Theta2, AmplitudeSqAvg, 'k--', linewidth=1)

#ax.plot(Theta2, np.zeros(40), 'ko', markersize=2)

plt.savefig("plot.png", bbox_inches='tight')

plt.show()
