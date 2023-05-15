import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=[8, 6])
ax = plt.gca()


#-- Set axis spines at 0
for spine in ['left', 'bottom']:
    ax.spines[spine].set_position('zero')
    ax.spines[spine].set_linewidth(2)
    
#-- Hide the other spines...
for spine in ['right', 'top']:
    ax.spines[spine].set_color('none')

#-- Decorate the spines
arrow_length = 20 # In points

#-- X-axis arrow
ax.annotate('Re{$z$}', fontsize=20, xy=(1, 0), xycoords=('axes fraction', 'data'), 
            xytext=(arrow_length, 0), textcoords='offset points',
            ha='left', va='center',
            arrowprops=dict(arrowstyle='<|-', fc='black',lw=2))

#-- Y-axis arrow
ax.annotate('Im{$z$}', fontsize=20, xy=(0, 1), xycoords=('data', 'axes fraction'), 
            xytext=(0, arrow_length), textcoords='offset points',
            ha='center', va='bottom',
            arrowprops=dict(arrowstyle='<|-', fc='black',lw=2))

#-- Plot
ax.axis([-0.33, 2, -0.33, +1])
ax.grid(False)
ax.set_aspect(1)


# Turn off ticks
ax.set_xticks([1.75])
ax.set_yticks([0.75])

# Turn off tick labels
ax.set_xticklabels(['$x$'],fontsize=20)
ax.set_yticklabels(['$y$'],fontsize=20)

#-- Function

theta = np.linspace(0, 2*np.pi, 100)

xc = np.cos(theta)
yc = np.sin(theta)

#ax.plot(2, 1, 'ks', markersize=5)

ax.arrow(0, 0, 1.75, 0.75, fc="k", ec="k",
         width=0.01, head_width=0.03, head_length=0.03,
         length_includes_head=True)

ax.annotate(r"$z=x+y$ j", (1.8,0.8), fontsize=20)

ax.plot(1.75,0,'k^',markersize=5)
ax.plot(0,0.75,'k>',markersize=5)

plt.savefig("plot.png", dpi=600, bbox_inches='tight')

plt.show()
