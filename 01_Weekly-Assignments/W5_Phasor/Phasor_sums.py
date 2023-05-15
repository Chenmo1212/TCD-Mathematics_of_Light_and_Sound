import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    num = 100000
    s_num = 10  # number of phasors that need to be summed

    mean = 0
    std = 0.2

    # generate random phasor with normal distribution
    tmp_r = np.random.normal(mean, std, size=(num, 1))
    tmp_i = np.random.normal(mean, std, size=(num, 1))

    # reshape phasor with s_sum and sum per row
    tmp_r = tmp_r.reshape(int(num / s_num), s_num)
    tmp_i = tmp_i.reshape(int(num / s_num), s_num)
    phasor_real = np.sum(tmp_r, axis=1)  # real part of the phasor
    phasor_imag = np.sum(tmp_i, axis=1)  # complex part of the phasor

    fig = plt.figure(figsize=(22, 7))
    plt.title('Random phasor sums based on the normal distribution', fontsize=18)

    ax1 = fig.add_subplot(131)
    ax1.set_xlim([-2.5, 2.5])
    ax1.set_ylim([-2.5, 2.5])
    ax1.set_xlabel('real')
    ax1.set_ylabel('imag')
    ax1.scatter(phasor_real, phasor_imag, s=2, c='red')

    ax2 = fig.add_subplot(132)
    ax2.set_xlabel('real')
    ax2.set_ylabel('count')
    ax2.hist(phasor_real, bins='auto')

    ax3 = fig.add_subplot(133)
    ax3.set_xlabel('imag')
    ax3.set_ylabel('count')
    ax3.hist(phasor_imag, bins='auto')

    plt.savefig('Random phasor sums based on the normal distribution')
