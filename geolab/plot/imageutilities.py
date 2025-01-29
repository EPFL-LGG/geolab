# -*- coding: utf-8 -*-

from __future__ import absolute_import

from __future__ import print_function

from __future__ import division

import numpy as np

from scipy.ndimage import gaussian_filter

# -----------------------------------------------------------------------------

__author__ = 'Davide Pellis'


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


def blur_shadow(img, blur=20, opacity=0.5):
    img[:, :, [0, 1, 2]] = 0.
    img[:, :, 3] = gaussian_filter(img[:, :, 3], sigma=blur) * opacity
    return img


def add_shadow(img, shadow):
    # img over shadow, https://en.wikipedia.org/wiki/Alpha_compositing
    h, w = img.shape[:2]
    new_alpha = img[:, :, 3] + (1.0 - img[:, :, 3]) * shadow[:, :, 3]
    img[:, :, :3] = (img[:, :, 3].reshape(h, w, 1) * img[:, :, :3] + (1.0 - img[:, :, 3].reshape(h, w, 1)) * shadow[:, :, 3].reshape(h, w, 1) * shadow[:, :, :3]) / (1.0e-12 + new_alpha.reshape(h, w, 1))
    img[:, :, 3] = new_alpha
    return img
