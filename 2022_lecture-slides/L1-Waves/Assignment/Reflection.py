# ===========================
# @Time    : 2022/09/12 12:12
# @Author  : Long Pan
# @Id      : 21332147
# @File    : Reflection.py
# ===========================


import numpy as np
import matplotlib.pyplot as plt
from pylab import rcParams


def set_plt_config():
    ax.set_xlim([-20, 120])
    ax.set_ylim([-10, 70])

    ax.set_yticks([])
    ax.set_xticks([])

    ax.set_yticklabels([])
    ax.set_xticklabels([])

    x_axis = np.linspace(-10, 110, 200)
    plt.plot(x_axis, 0 * x_axis, linewidth=4, color='#000000')
    plt.text(37.5, -6, 'Reflection', fontsize=22)


def draw_wave():
    x1 = np.linspace(0, 50, 100)
    y1 = -1 * x1 + 50

    x2 = np.linspace(50, 100, 100)
    y2 = 1 * x2 - 50

    plt.plot(x1, y1, linewidth=2, color='#4e9a06')
    plt.plot(x2, y2, linewidth=2, color='#4e9a06')


def draw_wave_border():
    x1_left = np.linspace(10, 30, 100)
    y1_left = -1 * x1_left + 30

    x1_right = np.linspace(30, 70, 100)
    y1_right = -1 * x1_right + 70

    x2_left = np.linspace(30, 70, 100)
    y2_left = 1 * x2_left - 30

    x2_right = np.linspace(70, 90, 100)
    y2_right = 1 * x2_right - 70

    plt.plot(x1_left, y1_left, linewidth=4, color='#babdb6')
    plt.plot(x1_right, y1_right, linewidth=4, color='#babdb6')
    plt.plot(x2_left, y2_left, linewidth=4, color='#babdb6')
    plt.plot(x2_right, y2_right, linewidth=4, color='#babdb6')


def draw_left_distance_line():
    for (index, i) in enumerate(np.linspace(15, 30, 4)):
        temp_x = np.linspace(i, i + 20, 100)
        temp_y = 1 * temp_x - (index * 10)

        # set wave color based on t
        c = '#ff4210' if index == t else '#ff4210' if index == 0 else '#204a87'
        plt.plot(temp_x, temp_y, linewidth=4, color=c)

        # add text description
        if c == '#ff4210':
            plt.text(temp_x[0] - 5, temp_y[0] - 5, 't=0', fontsize=20)

    for (index, i) in enumerate(np.linspace(40, 60, 3)):
        temp_x = np.linspace(i, i + 15 - index * 5, 100)
        temp_y = 1 * temp_x - (index * 10) - 40

        # set wave color based on t
        c = '#ff4210' if (index + 4) == t else '#204a87'
        plt.plot(temp_x, temp_y, linewidth=4, color=c)

        # add text description
        if c == '#ff4210':
            plt.text(temp_x[0] - 5, temp_y[0] - 5, 't=' + str(t), fontsize=20)


def draw_right_distance_line():
    for (index, i) in enumerate(np.linspace(50, 65, 4)):
        temp_x = np.linspace(i, i + 20, 100)
        temp_y = -1 * temp_x + (index * 10) + 70

        # set wave color based on t
        c = '#ff4210' if (index + 7) == t else '#204a87'
        plt.plot(temp_x, temp_y, linewidth=4, color=c)

        # add text description
        if c == '#ff4210':
            plt.text(temp_x[-1] + 3, temp_y[-1] - 3, 't=' + str(t), fontsize=20)


def draw_arrow():
    x_entrance = np.linspace(3, 30, 100)
    y_entrance = -1 * x_entrance + 50
    plt.plot(x_entrance, y_entrance, linewidth=4, color='#204a87', linestyle="--")

    # add arrow after the line
    ax.arrow(x_entrance[-1], y_entrance[-1], 1, -1, head_width=2.5, head_length=2.5, fc='#204a87', ec='#204a87',
             length_includes_head=True)

    x_exit = np.linspace(70, 97, 100)
    y_exit = 1 * x_exit - 50
    plt.plot(x_exit, y_exit, linewidth=4, color='#4e9a06', linestyle="--")

    # add arrow after the line
    ax.arrow(x_exit[-1], y_exit[-1], 1, 1, head_width=2.5, head_length=2.5, fc='#4e9a06', ec='#4e9a06',
             length_includes_head=True)


def draw_circle():
    plt.plot([30, 40, 50, 60], [0, 0, 0, 0], 'o', color="#edd400")
    draw_circle_wave(30, [4, 8, 12, 16])
    draw_circle_wave(40, [4, 8, 12])
    draw_circle_wave(50, [4, 8])
    draw_circle_wave(60, [4])


def draw_circle_wave(c, r_list):
    for r in r_list:
        for phi in np.linspace(0, np.pi, 200):
            x = c + r * np.cos(phi)
            y = r * np.sin(phi)
            plt.scatter(x, y, s=1, color='#babdb6', linewidths=2)


if __name__ == '__main__':
    # Set wave time
    t = 9

    # 1. Set the configuration information of a plot
    rcParams['figure.figsize'] = 16, 9
    ax = plt.gca()
    set_plt_config()

    # 2. Draw wave and its border
    draw_wave()
    draw_wave_border()

    # 3. Draw the distance of wave
    draw_left_distance_line()
    draw_right_distance_line()

    # 4. Draw the circle wave
    draw_arrow()
    draw_circle()

    # 5. Show the plot
    plt.show()
