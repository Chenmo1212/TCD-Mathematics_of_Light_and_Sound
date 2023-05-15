import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import expon

for i in [2**0, 2**2, 2**4, 2**6, 2**8, 2**10, 2**12, 2**14, 2**16]:

    xy = np.zeros((120, 160),dtype='f')
    
    for j in range(1,i+1):

#        print("i is %d, j is %d" % (i, j))
        
        xy += expon.rvs(scale=1.0,size=[120, 160])

    xy = xy/i

    xymean= np.mean(xy)
    xystd= np.std(xy)
    xymax= np.max(xy)
    xyC = xystd/xymean
    
    print(i, xymean, xystd, xymax, xyC)
    
#    xy[xy>1.75]=1.75

    fig = plt.figure(figsize=[8, 6])
    ax = plt.gca()
    ax.set_aspect(1)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    
    plt.imshow(xy, origin='lower', #extent=(-200,+200,-150,+150),
               cmap='gray', aspect='equal',
               vmin=0.8,
               vmax=1.2)
    
    plt.savefig("plot-Image-%d.png"%i, dpi=600, bbox_inches='tight')
    plt.show()

# plt.figure()
# plt.hist(xy, bins=60, fc='k', ec='k')
# plt.savefig("plot-Hist.png", dpi=600, bbox_inches='tight')
# plt.show()
