import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    num = 100000
    s_num = 10  # number of phasors that need to be summed

    scale = 5

    # generate random phasors with rayleigh distribution
    tmp = np.random.rayleigh(scale, num)

    # reshape phasors with s_sum and sum per row
    tmp = tmp.reshape(int(num / s_num), s_num)
    intensity_list = np.sum(tmp, axis=1)

    fig = plt.figure(figsize=(8, 8))
    plt.title('Rayleigh Distribution of Wave Resultant Intensities')
    plt.xlabel('Intensity')
    plt.ylabel('Frequency')

    plt.hist(intensity_list, bins='auto')
    plt.show()
    # plt.savefig('Q3_Rayleigh_Distribution_of_Wave_Resultant_Intensities')

