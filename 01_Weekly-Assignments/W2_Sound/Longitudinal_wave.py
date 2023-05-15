import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np


def plot_init(show_axis=True):
    for spine in ['left', 'right', 'top', 'bottom']:
        ax.spines[spine].set_color('none')

    # plt.axhline(0, color='black')
    # plt.axvline(0, color='black', linestyle='--')

    ax.set_xlim([0, x_axis + 0.5])
    ax.set_ylim([-1.5 - y_axis / 2, y_axis / 2 + 1.5])

    # Turn off ticks
    if not show_axis:
        ax.set_yticks([])
        ax.set_xticks([])


def create_points_pos(xn=30, yn=5, xa=30, ya=10):
    """
    generate points randomly
    :param xn: x axis points number
    :param yn: y axis points number
    :param xa: x axis range
    :param ya: y axis range
    :return:
    """
    pp = []
    for i in range(xn):
        for j in range(yn):
            x = np.random.uniform(0, xa)
            y = np.random.uniform(-ya / 2, ya / 2)
            pp.append([x, y])
    return np.array(pp)


def init():
    sca.set_offsets(list(points_pos))
    label = "time step {0}".format(0)
    ax.set_xlabel(label)
    return sca, ax


def animate(frame):
    return plot_wave_at_time(frame, points_pos)


def plot_wave_at_time(frame, pp):
    """
    plot wave at the specific frame
    :param frame: specific time
    :param pp: points position list
    :return:
    """
    arr = np.copy(pp)

    k = 2 * np.pi / wave_len
    w = 2 * np.pi / wave_frequency

    for i in range(len(arr)):  # update the position of every point
        x = arr[i][0]
        # update point position use 'R * cos(kx − ωt) + (1 − R) * cos(kx + ωt)'
        arr[i][0] = arr[i][0] + R * np.cos(k * x - w * frame) + (1 - R) * np.cos(k * x + w * frame)

    sca.set_offsets(np.c_[arr[:, 0], arr[:, 1]])
    label = "time step {0}".format(frame)
    ax.set_xlabel(label, fontsize=18)
    return sca, ax


if __name__ == '__main__':
    # set up the parameters of random points
    x_num = 300
    y_num = 30
    x_axis = 50
    y_axis = 10

    # create points
    points_pos = create_points_pos(x_num, y_num, x_axis, y_axis)

    # init the plot
    fig, ax = plt.subplots(figsize=(18, 7.5))
    plot_init(show_axis=False)

    sca = ax.scatter([], [], 10, c='#000000')

    # ==========================  display the wave animation =====================

    # set up wave parameters
    wave_frequency = 200  # frequency
    wave_len = 10  # wave length
    R = 0.8  # |R| <= 1, wave direction(R>=0.5-left, R<=0.5-right)

    # create the wave animation
    ani = animation.FuncAnimation(fig=fig, func=animate, frames=100, init_func=init, interval=30, blit=False)

    # I need to add "block=True" to display the animation in my laptop, but maybe u don't need it
    plt.show(block=True)
    ani.save('Longitudinal_wave.gif', writer='pillow')

    # ===================  display the wave at a specific time i =================
    # need to comment out the animation part above

    # t = 3
    # plot_wave_at_time(t, points_pos)
    # plt.savefig('Longitudinal_wave_at_time_{}'.format(t))

