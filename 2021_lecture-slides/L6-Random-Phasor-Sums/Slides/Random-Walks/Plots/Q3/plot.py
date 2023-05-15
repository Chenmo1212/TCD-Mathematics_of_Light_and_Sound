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
ax.annotate(r'$\cos\phi$', fontsize=20, xy=(1, 0), xycoords=('axes fraction', 'data'), 
            xytext=(arrow_length, 0), textcoords='offset points',
            ha='left', va='center',
            arrowprops=dict(arrowstyle='<|-', fc='black',lw=2))

#-- Y-axis arrow
ax.annotate(r'j $\sin\phi$', fontsize=20, xy=(0, 1), xycoords=('data', 'axes fraction'), 
            xytext=(0, arrow_length), textcoords='offset points',
            ha='center', va='bottom',
            arrowprops=dict(arrowstyle='<|-', fc='black',lw=2))

#-- Plot
theta = np.linspace(-0.75*np.pi, 0.75*np.pi, 100)
ax.axis([theta[0], theta[-1], -0.25, +3])

# Turn off ticks
ax.set_xticks([])
ax.set_yticks([])

# Turn off tick labels
ax.set_xticklabels([])
ax.set_yticklabels([])

ax.grid(False)
ax.set_aspect(1)

CosCoef = 0
SinCoef = 0

# Amp = [+1.5, +2.5, -1.25, +1.5, -1.25]
# Phi = [+1.25, +3.0, -2.0, -0.5, -0.75]

Amp = [+1.5, +2.0, +1.25, +1.0, 1.75]
Phi = [+0.5, +2.0, +3.0, -0.5, +3.5]

np.set_printoptions(precision=4)

for idx, val in enumerate(Amp):

#     if idx == 2: break
     
     print(idx, 'start:', CosCoef, SinCoef)

     ax.arrow(CosCoef, SinCoef,
              Amp[idx]*np.cos(Phi[idx]),
              Amp[idx]*np.sin(Phi[idx]),
              fc="k", ec="k", width=0.03,
              head_width=0.12, head_length=0.12,
              length_includes_head=True)

 #    ax.plot(theta, Amp[idx]*np.cos(theta-Phi[idx]),'k-')

     CosCoef = CosCoef+Amp[idx]*np.cos(Phi[idx])
     SinCoef = SinCoef+Amp[idx]*np.sin(Phi[idx])

     print(idx, 'End:', CosCoef, SinCoef)
     
ax.arrow(0, 0, CosCoef, SinCoef, fc="k", ec="k", ls="-", lw=4,
         width=0.03, head_width=0.12, head_length=0.12,
         length_includes_head=True)

AmpResultant = np.sqrt(np.square(CosCoef)+np.square(SinCoef))
PhiResultant = np.angle(np.complex(CosCoef,SinCoef))

print('Amp, Phi', AmpResultant, PhiResultant)

#ax.plot(theta, AmpResultant*np.cos(theta-PhiResultant),'k-', linewidth=4)

     
#     print(i)

plt.savefig("plot-destructive.png", dpi=600, bbox_inches='tight')
plt.show()
