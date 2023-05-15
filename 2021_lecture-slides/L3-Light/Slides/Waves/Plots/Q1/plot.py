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
ax.annotate('$y$', xy=(0, 1), xycoords=('data', 'axes fraction'), 
            xytext=(0, arrow_length), textcoords='offset points',
            ha='center', va='bottom',
            arrowprops=dict(arrowstyle='<|-', fc='black'))

#-- Plot
ax.axis([-5.25*np.pi/2, 7.6*np.pi, -1.6*np.pi, 3.6*np.pi])
ax.grid(False)
ax.set_aspect(1)


# Turn off ticks
ax.set_yticks([])
ax.set_xticks([])

# Turn off tick labels
ax.set_yticklabels([])
ax.set_xticklabels([])

#-- Function

for wave in range(1,5):

    theta = np.linspace(0, 2*np.pi, np.int(10*wave*2*np.pi))

    r_hi = wave*2*np.pi - (3*np.pi/2)
    r_lo = wave*2*np.pi - (np.pi/2)

    x_hi = r_hi*np.cos(theta)
    y_hi = r_hi*np.sin(theta)

    x_lo = r_lo*np.cos(theta)
    y_lo = r_lo*np.sin(theta)

    if wave==2: 
        ax.plot(x_hi, y_hi, 'k-', linewidth=2)
        ax.plot(x_lo, y_lo, 'k--', linewidth=2)
    else:
        ax.plot(x_hi, y_hi, 'k-', linewidth=1)
        ax.plot(x_lo, y_lo, 'k--', linewidth=1)

plt.savefig("plot.png", bbox_inches='tight')

plt.show()
