#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-06 10:38:13
# @Author  : Yan Liu & Zhi Liu (zhiliu.mind@gmail.com)
# @Link    : http://iridescent.ink
# @Version : $1.0$
#
#

import pyopt as pyo
import numpy as np
from scipy.misc import imread

imgfile = '../../data/img/cameraman.tif'

X = imread(imgfile)

X = X[0:16, 0:16]

[M, N] = X.shape
print(X.shape)

h = np.ones((1, 9))

lh = np.size(h)

h = h / np.sum(h)

h = np.concatenate((h, np.zeros((1, M - lh))), axis=1)
print(h.shape)

h = pyo.cshift(h, -(lh - 1) / 2)

h = np.matmul(h.transpose(), h)
# print(h[3:10,3:9])
HFFT = np.fft.fft2(h)
HCFFT = np.conj(HFFT)
print(HFFT.shape, HCFFT.shape)

A = lambda x: np.real(np.fft.ifft2(HFFT * np.fft.fft2(x)))
AH = lambda x: np.real(np.fft.ifft2(HCFFT * np.fft.fft2(x)))

# observation
Ax = A(X)
Psig = np.linalg.norm(Ax, ord='fro') ** 2 / (M * N)

BSNRdb = 40

sigma = np.linalg.norm(Ax - np.mean(Ax.flatten()), ord='fro') / \
    np.sqrt(M * N * 10 ** (BSNRdb / 10.0))

print(Psig, sigma)

y = Ax + sigma * np.random.randn(M, N)

# algorithm parameters
c = 2.5e-2  # reg parameter
mu = c / 10
outeriters = 500
tolerror = 1e-5


def ddd(X):
    X = 0
    return 0

Tvx = pyo.tvnorm(X)
ddd(X)
print(X)
chambolleit = 5
print(Tvx)
