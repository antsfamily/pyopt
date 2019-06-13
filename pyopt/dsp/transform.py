#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-06 10:38:13
# @Author  : Yan Liu & Zhi Liu (zhiliu.mind@gmail.com)
# @Link    : http://iridescent.ink
# @Version : $1.0$
from __future__ import division, print_function, absolute_import
import numpy as np


def fft(s, n=None, axis=-1):
    r"""
    Improved fft that gives the correct phase
    Input signal should be such that the element s[middle] corresponds to the time = 0
    """
    # return np.fft.fftshift(np.fft.fft(np.fft.fftshift(s), n, axis=axis))
    return np.fft.fftshift(np.fft.fft(np.fft.fftshift(s, axes=axis), n, axis=axis), axes=axis)


def ifft(s, n=None, axis=-1):
    r"""
    Improved ifft that gives the correct phase
    Input signal should be such that the element s[middle] corresponds to the frequency = 0
    """
    return np.fft.ifftshift(np.fft.ifft(np.fft.ifftshift(s, axes=axis), n, axis=axis), axes=axis)


def freq(length, bandwidth):
    # return np.fft.fftfreq(length, 1.0 / bandwidth)
    return np.fft.fftshift(np.fft.fftfreq(length, 1.0 / bandwidth))


def fft2(img):
    r"""
    Improved 2D fft
    """
    out = np.zeros(img.shape, dtype=complex)
    for i in range(out.shape[1]):
        # get range fixed column
        out[:, i] = fft(img[:, i])
    for j in range(out.shape[0]):
        out[j, :] = fft(out[j, :])
    return out


def ifft2(img):
    r"""
    Improved 2D ifft
    """
    out = np.zeros(img.shape, dtype=complex)
    for i in range(out.shape[1]):
        out[:, i] = ifft(img[:, i])
    for j in range(out.shape[0]):
        out[j, :] = ifft(out[j, :])
    return out


def fftx(x, n=None):

    return np.fft.fftshift(np.fft.fft(np.fft.fftshift(x, n)))


def ffty(x, n=None):
    return (np.fft.fftshift(np.fft.fft(np.fft.fftshift(x.transpose(), n)))).transpose()


def ifftx(x, n=None):
    return np.fft.fftshift(np.fft.ifft(np.fft.fftshift(x), n))


def iffty(x, n=None):
    return (np.fft.fftshift(np.fft.ifft(x.transpose(), n))).transpose()
