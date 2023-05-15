import numpy as np
import matplotlib.pyplot as plt


def get_intensity(lambda_):
    return np.exp(-nums * lambda_) * lambda_


def get_sum_intensity(l1, l2):
    if l1 == l2:
        # f_z = z * λ^2 * exp(−λ * z)
        return nums * l1 ** 2 * np.exp(-nums * l1)
    else:
        # f_z = λX * λY / (λY − λX) * (exp(−z * λX) − exp(−z * λY))
        return (l2 * l1) / (l1 - l2) * (np.exp(-nums * l2) - np.exp(-nums * l1))


if __name__ == '__main__':
    nums = np.arange(0, 10, 0.1)

    fig = plt.figure(figsize=(10, 5))
    fig.suptitle('Probability density of the sum of the wave resultant intensities', fontsize=14)

    ax1 = fig.add_subplot(121)
    plt.plot(nums, get_intensity(1), label="I1")
    plt.plot(nums, get_intensity(2), label="I2")
    plt.plot(nums, get_sum_intensity(2, 1), label="I1+I2")
    plt.title("Result of λ1 != λ2")
    plt.legend()

    ax2 = fig.add_subplot(122)
    plt.plot(nums, get_intensity(1), label="I1&I2")
    plt.plot(nums, get_sum_intensity(1, 1), label="I1+I2")
    plt.title("Result of λ1 == λ2")
    plt.legend()

    plt.show()

