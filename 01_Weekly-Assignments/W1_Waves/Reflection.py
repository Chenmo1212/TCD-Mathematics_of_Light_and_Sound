import numpy as np
from matplotlib.patches import Wedge
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt


def plot_init(show_axis=True):
    for spine in ['left', 'right', 'top', 'bottom']:
        ax.spines[spine].set_color('none')

    plt.axhline(0, color='black')
    plt.axvline(2, color='black', linestyle='--')

    plt.xlim(-4.0, 8.0)
    plt.ylim(0, 6.0)

    # Turn off ticks
    if show_axis:
        ax.set_yticks([])
        ax.set_xticks([])


def get_out_angle(angle, ref1, ref2):
    """
    Calculate the out angle by different refractive index
    """
    print('out angle is %s' % (90 - np.arcsin(np.sin(angle) * ref1 / ref2) * 180))
    return np.arcsin(np.sin(angle) * ref1 / ref2)


def plot_top_boundaries(ina, width):
    top_x = 5 * np.sin(ina)
    top_y = 5 * np.cos(ina)
    ax.plot([-top_x, 0], [top_y, 0], color='#babdb6')
    ax.plot([-top_x*1.6 + width, width], [top_y*1.6, 0], color='#babdb6')

    # draw the top arrow
    ax.arrow((-top_x*2.6 + width) / 2, top_y*1.3, width * np.sin(ina), width * -np.cos(ina),
             head_width=0.1, color='blue')


def plot_top_incident(outa, ina, width):
    dx_top = - 1 + np.cos(ina) ** 2
    dy_top = np.sin(ina) * np.cos(ina)

    points = []
    for i in range(-4, 6):
        if i > 0:
            x = dx_top * i
            y = dy_top * i
        else:
            x = -i
            y = 0

            # draw the scatter points
            ax.scatter(x, 0, color='#edd400', zorder=5)
            points.append(x)

        if i == 5:
            plt.annotate("t=0", (dx_top * (width + i) + width, (width + i) * dy_top), fontsize=18)
            color = 'red'
        elif i + t == 5:
            plt.annotate("t={}".format(t), (dx_top * (width + i) + width, (width + i) * dy_top), fontsize=18)
            color = 'red'
        else:
            color = '#204a87'

        ax.plot([x, dx_top * (width + i) + width], [y, (width + i) * dy_top], color=color, linewidth=2)

    # draw the wave of scatter points
    plot_point_wave(points, outa)


def plot_point_wave(scatter, outa):
    # draw the wave part
    patches = []
    for i in range(len(scatter) - 1):
        for j in range(len(scatter) - 1 - i, 0, -1):
            wedge = Wedge((i, 0), j * np.sin(outa), 0, 180, color='gray', fill=False, alpha=0.2 * (i + j))
            patches.append(wedge)
    p = PatchCollection(patches, match_original=True)
    ax.add_collection(p)


def plot_bottom_boundaries(outa, width):
    bottom_x = 5 * np.sin(outa)
    bottom_y = 5 * np.cos(outa)
    ax.plot([0, bottom_x * 1.5], [0, bottom_y * 1.5], color='#babdb6')
    ax.plot([0 + width, bottom_x + width], [0, bottom_y], color='#babdb6')

    ax.arrow(0 + width / 2, 0, width * np.sin(outa), width * np.cos(outa), head_width=0.1,
             color='blue')


def plot_bottom_incident(outa, width):
    dx_bottom = np.sin(outa) ** 2
    dy_bottom = 1 * np.sin(outa) * np.cos(outa)
    init_x = width * dx_bottom
    init_y = width * dy_bottom

    for i in range(0, 8):
        if t - i == 9:
            color = 'red'
            plt.annotate("t={}".format(t), (width + dx_bottom * i, dy_bottom * i), fontsize=18)
        else:
            color = '#4e9a06'

        ax.plot([init_x + dx_bottom * i, width + dx_bottom * i],
                [init_y + dy_bottom * i, dy_bottom * i], color=color, linewidth=2)


def plot_reflection(in_rad, r1, r2, width=4):
    # get_out_angle
    out_rad = in_rad

    # plot the top boundaries and arrow
    plot_top_boundaries(in_rad, width)

    # draw the top incident
    plot_top_incident(out_rad, in_rad, width)

    # draw the bottom lines
    plot_bottom_boundaries(out_rad, width)

    # draw the bottom incident
    plot_bottom_incident(out_rad, width)

    plt.title('Plot of wave reflection based on Huygens-Fresnel Construction from ref {} to ref {}'.format(ref1, ref2), fontsize=20)
    plt.savefig('Reflection')
    plt.show()


if __name__ == '__main__':
    fig, ax = plt.subplots(figsize=(16, 8))
    plot_init(show_axis=True)

    in_angle = 30
    ref1 = 1
    ref2 = 1.516
    t = 15  # 0 <= t <= 16

    plot_reflection(np.deg2rad(in_angle), ref1, ref2)
