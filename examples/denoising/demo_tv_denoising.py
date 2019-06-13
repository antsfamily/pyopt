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

[M, N] = X.shape
print(X.shape)




# algorithm parameters
c = 2.5e-2  # reg parameter
mu = c / 10
outeriters = 500
tolerror = 1e-5

Tvx = pyo.tvnorm(X)
chambolleit = 5
print(Tvx)
