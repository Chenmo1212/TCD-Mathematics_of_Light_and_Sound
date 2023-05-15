import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import expon

fig = plt.figure(figsize=[8, 6])
ax = plt.gca()

#-- Plot
# ax.axis([-3,3,-3,3])
# ax.grid(False)
ax.set_aspect(1)

# axis labels
# ax.set_xlabel()
# ax.set_ylabel()

# Turn off ticks
ax.set_xticks([])
ax.set_yticks([])

# Turn off tick labels
ax.set_xticklabels([])
ax.set_yticklabels([])

xy = expon.rvs(scale=1.0,size=[120, 160])

xy3 = np.copy(xy)
xy3[xy3>4.0]=4.0

plt.imshow(xy3, origin='lower', #extent=(-200,+200,-150,+150),
           cmap='gray',label='test',aspect='equal')

plt.savefig("plot-Image.png", dpi=600, bbox_inches='tight')
plt.show()

print(np.mean(xy), np.std(xy), np.sum(xy[xy>4.0]), np.amax(xy))

plt.figure()
plt.hist(xy, bins=60, fc='k', ec='k')
plt.savefig("plot-Hist.png", dpi=600, bbox_inches='tight')
plt.show()
