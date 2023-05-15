# ===========================
# @Time    : 2022/09/02 12:12
# @Author  : Long Pan
# @Id      : 21332147
# @File    : Light.py
# ===========================
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from mpl_toolkits.mplot3d import Axes3D


def update(frame):
    ax.clear()
    ax.set(xlim=[0, max_length], ylim=[-amplitude, amplitude], zlim=[-amplitude, amplitude])

    t = frame / frame_rate
    x = plot_speed * t
    if len(xs) < max_count:
        xs.append(x)

    ys.append(amplitude * np.sin(omega * x))
    if len(ys) > max_count:
        del (ys[0])

    ax.plot(xs, -1 * np.array(ys), zdir='z', color='#06d6a0')
    ax.plot(xs, ys, zdir='y', color='#118ab2')
    ax.plot(xs, np.zeros(len(xs)), zdir='z', color='#ef476f')

    fig.suptitle('electromagnetic field')


if __name__ == '__main__':
    frame_rate = 30

    amplitude = 5
    omega = 2

    plot_speed = 2
    max_length = 10
    gap = plot_speed / frame_rate
    max_count = int(max_length / gap)

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.get_proj = lambda: np.dot(Axes3D.get_proj(ax), np.diag([1, 0.5, 0.5, 0.8]))
    ax.view_init(15, -54)

    xs = []
    ys = []

    ani = anim.FuncAnimation(fig, update, interval=1000 / frame_rate)
    # ani.save('Light.gif', writer='pillow')
    plt.show(block=True)
