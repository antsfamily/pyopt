from __future__ import division, print_function, absolute_import
import numpy as np
from scipy import signal


def cshift(x, L):

    N = np.size(x)

    if np.size(x, 0) > 1:
        raise ValueError("Input x must be 1-d vector!")

    L = int(L)

    y = np.zeros(x.shape)
    print(x.shape, y.shape)

    if L == 0:
        y = x

    if L > 0:
        y[0, L:-1] = x[0, 0:N - L]
        y[0, 0:L] = x[0, N - L:N]
    else:
        L = -L
        y[0, 0:N - L] = x[0, L:N]
        y[0, N - L:N] = x[0, 0:L]

    return y


def diffh(x):

    h = np.array([[0, 1, -1]])
    return cconv2(x, h)


def diffv(x):

    h = np.array([[0, 1, -1]])
    h = h.transpose()
    return cconv2(x, h)


def _wraparound(x, h):
    """_wraparound

    Extend x so as to wrap around on both axes, sufficient to allow a
    "valid" convolution with m to return the cyclical convolution.
    We assume mask origin near centre of mask for compatibility with
   "same" option.

    Arguments:
        x {ndarray} -- signal matrix
        h {1d array} -- filters
    """

    # print(x.shape, h.shape)
    mx, nx = x.shape
    mh, nh = h.shape
    if mh > mx or nh > nx:
        raise ValueError("Mask does not fit inside array!")

    mo = int(np.floor((1 + mh) / 2))
    no = int(np.floor((1 + nh) / 2))
    m1 = int(mo - 1)
    n1 = int(no - 1)
    mr = int(mh - mo)
    nr = int(nh - no)
    me = int(mx - m1 + 1)
    ne = int(nx - n1 + 1)
    mt = int(mx + m1)
    nt = int(nx + n1)
    my = int(mx + mh - 1)
    ny = int(nx + nh - 1)

    # print(mh, nh)
    # print(mo, no, m1, n1, mr, nr, me, ne, mt, nt, my, ny)

    y = np.zeros((my, ny))
    y[mo - 1:mt, no - 1:nt] = x
    if m1 > 0:
        y[0:m1, no - 1:nt] = x[me - 1:mx, :]
        if n1 > 0:
            y[0:m1, 0:n1] = x[me - 1:mx, ne - 1:nx]
        if nr > 0:
            y[0:m1, nt:ny] = x[me - 1:mx, 0:nr]

    if mr > 0:
        y[mt:my, no - 1:nt] = x[0:mr, :]
        if n1 > 0:
            y[mt:my, 0:n1] = x[0:mr, ne - 1:nx]
        if nr > 0:
            y[mt:my, nt:ny] = x[0:mr, 0:nr]

    if n1 > 0:
        y[mo - 1:mt, 0:n1] = x[:, ne - 1:nx]
    if nr > 0:
        y[mo - 1:mt, nt:ny] = x[:, 0:nr]
    return y


def cconv2(x, h, mod='valid'):
    r"""Circular 2D convolution

    Circular 2D convolution

    Arguments:
       x {ndarray} -- signal matrix
       h {1d array} -- filters

    Keyword Arguments:
       mod {str} -- mode (default: {'valid'})
    """

    x = _wraparound(x, h)
    return signal.convolve2d(x, h, mod)
