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
ax.axis([-4*np.pi, 4*np.pi, -7.2, +7.2])
ax.grid(False)
ax.set_aspect(1)


# Turn off ticks
ax.set_yticks([])
ax.set_xticks([])

# Turn off tick labels
ax.set_yticklabels([])
ax.set_xticklabels([])

#-- Function

PhaseCutPosition = 0.5*np.pi
PhaseCutHalf = 0.3333*np.pi # Should have two of these for appropriate cancellation of pos and neg.
PhaseShift = -0.3333*np.pi  # Change theta array proportions if changing this.

PosThetaForward = np.linspace(0, 4*np.pi, 396)
PosThetaBackward = np.linspace(-4*np.pi, 0, 396)

PosAmplitudeForward = 3.5*np.sin(PosThetaForward+(PhaseCutPosition+PhaseCutHalf))
PosAmplitudeBackward = 3.5*np.sin(PosThetaBackward+(PhaseCutPosition-PhaseCutHalf))

#ax.plot(PosThetaForward, PosAmplitudeForward, 'k--', linewidth=1)
#ax.plot(PosThetaBackward, PosAmplitudeBackward, 'k--', linewidth=1)

#plt.savefig("plot-increasing.png", dpi=1200, bbox_inches='tight')

NegThetaForward = np.linspace(PhaseShift, 4*np.pi, (396+33)) # change number of samples to take into
NegThetaBackward = np.linspace(-4*np.pi, PhaseShift, (396-33)) # account the phase shift

NegAmplitudeForward = 3.5*np.sin(NegThetaForward+(PhaseCutPosition-PhaseCutHalf-PhaseShift))
NegAmplitudeBackward = 3.5*np.sin(NegThetaBackward+(PhaseCutPosition+PhaseCutHalf-PhaseShift))

#ax.plot(NegThetaForward, NegAmplitudeForward, 'k:', markersize=1)
#ax.plot(NegThetaBackward, NegAmplitudeBackward, 'k:', markersize=1)

#plt.savefig("plot-decreasing.png", dpi=1200, bbox_inches='tight')

AllTheta = np.linspace(-4*np.pi, +4*np.pi, 792)
NegAmplitude = np.concatenate((NegAmplitudeBackward, NegAmplitudeForward))
PosAmplitude = np.concatenate((PosAmplitudeBackward, PosAmplitudeForward))

ax.plot(AllTheta, PosAmplitude+NegAmplitude, 'k-', linewidth=1.25)
plt.savefig("plot-propagation.png", dpi=1200, bbox_inches='tight')

plt.show()
