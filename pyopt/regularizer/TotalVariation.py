from __future__ import division, print_function, absolute_import
import numpy as np
import pyopt as pyo


def tvnorm(x):

    print("===TV norm")

    y = np.sum(np.sum(np.sqrt(pyo.diffh(x) ** 2 + pyo.diffv(x) ** 2)))
    x = 0
    return y
