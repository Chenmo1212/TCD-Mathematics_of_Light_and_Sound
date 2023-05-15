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
ax.annotate('$\Re$', fontsize=20, xy=(1, 0), xycoords=('axes fraction', 'data'), 
            xytext=(arrow_length, 0), textcoords='offset points',
            ha='left', va='center',
            arrowprops=dict(arrowstyle='<|-', fc='black',lw=2))

#-- Y-axis arrow
ax.annotate('$\Im$', fontsize=20, xy=(0, 1), xycoords=('data', 'axes fraction'), 
            xytext=(0, arrow_length), textcoords='offset points',
            ha='center', va='bottom',
            arrowprops=dict(arrowstyle='<|-', fc='black',lw=2))

#-- Plot
ax.axis([-2, 6, -2, 8])
ax.grid(False)
ax.set_aspect(1)


# Turn off ticks
ax.set_xticks([])
ax.set_yticks([])

# Turn off tick labels
ax.set_xticklabels([])
ax.set_yticklabels([])

xh = 0
yh = 0

#xt = [+3, -4, -1, +5]
#yt = [+2, +1, +3, +1]

xt = [+3, +1, -3, +0.5, -2.5]
yt = [+2, +3, -1, -1, -0.5]

for idx, val in enumerate(xt,start=0):

#     if idx == 2: break
     
     print(idx, 'start ', xh, yh)
     print(idx, 'end ', xh+xt[idx], yh+yt[idx])

     ax.arrow(xh, yh, xt[idx], yt[idx], fc="k", ec="k",
              width=0.03, head_width=0.12, head_length=0.12,
              length_includes_head=True)

     xh = xh+xt[idx]
     yh = yh+yt[idx] 

ax.arrow(0, 0, xh, yh, fc="k", ec="k", ls="-", lw=6,
         width=0.03, head_width=0.12, head_length=0.12,
         length_includes_head=True)

#     print(i)

plt.savefig("plot-destructive.png", dpi=600, bbox_inches='tight')
plt.show()
