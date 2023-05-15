# https://blog.csdn.net/jk_101/article/details/124804014
import numpy as np
import matplotlib.pyplot as plt
import math

from numpy.fft import fft2


def get_shape(img_, shape_type):
    h, w = img_.shape
    for i in range(h):
        for j in range(w):
            # According to different shapes, use different conditional statements
            # to assign a value of 255 to a specific area
            if shape_type == 'triangle':
                img[i][j] = 255 if (95 < i < 105 and 95 < j < i) else 0
            elif shape_type == 'circle':
                img[i][j] = 255 if ((i - 100) ** 2 + (j - 100) ** 2 <= 50) else 0
            elif shape_type == 'square':
                img[i][j] = 255 if (95 < i < 105 and 95 < j < 105) else 0

            # Increase the contrast between light and dark
            img[i][j] = img[i][j] * math.pow(-1, i + j)


def draw_shape(img_, shape):
    get_shape(img_, shape)

    ax1 = fig.add_subplot(121)
    ax1.imshow(np.abs(img_), cmap='gray')
    ax1.set_title('{} aperture'.format(shape))

    ax2 = fig.add_subplot(122)
    img_ = fft2(img_)
    ax2.imshow(np.abs(img_), cmap='gray')
    ax2.set_title('{} diffraction'.format(shape))


if __name__ == '__main__':
    fig = plt.figure(figsize=(8, 4))
    img = np.zeros((200, 200))

    shape = 'square'  # 'circle' / 'square'
    draw_shape(img, shape)

    fig.suptitle('Diffraction pattern of a {} aperture'.format(shape), fontsize=14)
    plt.savefig('Diffraction pattern of a {} aperture'.format(shape))
    plt.show()
