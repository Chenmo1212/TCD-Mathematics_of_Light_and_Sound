import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=[8, 6])
ax = plt.gca()

#-- Plot
# ax.axis([-3,3,-3,3])
# ax.grid(False)
# ax.set_aspect(1)

# axis labels
ax.set_xlabel("$R$")
ax.set_ylabel("$I$")

# Turn off ticks
ax.set_xticks([-33, -17, 0, 17, 33])
ax.set_yticks([-33, -17, 0, 17, 33])

# Turn off tick labels
ax.set_xticklabels(['-2', '-1', '0', '+1', '+2'])
ax.set_yticklabels(['-2', '-1', '0', '+1', '+2'])

x = np.linspace(-3, +3, 200)
y = np.linspace(-3, +3, 200)

xx, yy = np.meshgrid(x, y)

std_x = 1.
std_y = 1.
A = 1/(2*np.pi)

Gaussian = A * np.exp(-(xx**2/(2*std_x**2) + yy**2/(2*std_y**2)))

#Gaussian = np.sqrt(xx**2 + yy**2)

#ax.legend([plt.Rectangle((0,0),0,0,0)],["step0"], loc='upper right',prop={'size':12})

plt.imshow(Gaussian, origin='lower',extent=(-50,+50,-50,+50),
           cmap='Greys',label='test')


#plt.contour(xx,yy, Gaussian, colors='k', levels=15, linewidths=1)
#plt.plot(xx,yy,'k.',markersize=1)

plt.savefig("plot.png", dpi=600, bbox_inches='tight')
plt.show()
