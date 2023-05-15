import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=[8, 6])
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
ax.axis([-1.2, +1.2, -1.2, +1.2])
ax.grid(False)
ax.set_aspect(1)


# Turn off ticks
ax.set_yticks([1])
ax.set_xticks([])

# Turn off tick labels
ax.set_yticklabels(['$1$'])
ax.set_xticklabels([])

#-- Function

theta = np.linspace(0, 2*np.pi, 100)

xc = np.cos(theta)
yc = np.sin(theta)

ax.plot(xc, yc, 'k-', linewidth=1)

ax.plot([0, xc[66]], [0, yc[66]], 'k-', linewidth=1)
ax.annotate(r"$(x,y)$",(-0.85,-1.1))

ax.plot(0.25*xc[0:66], 0.25*yc[0:66], 'k-', linewidth=1)
ax.annotate(r"$\theta$",(-0.25,+0.25))


ax.plot(xc[66],yc[66],'ks',markersize=5)

ax.plot(0,yc[66],'k<',markersize=5)
ax.plot(xc[66],0,'kv',markersize=5)

plt.savefig("plot.png", dpi=600, bbox_inches='tight')

plt.show()
