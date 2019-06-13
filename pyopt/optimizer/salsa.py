#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-06 10:38:13
# @Author  : Yan Liu & Zhi Liu (zhiliu.mind@gmail.com)
# @Link    : http://iridescent.ink
# @Version : $1.0$
#
# @Note    : http://cascais.lx.it.pt/~mafonso/salsa.html
#
from __future__ import division, print_function, absolute_import
import numpy as np


class Salsa(object):

    r"""Split Augmented Lagrangian Shrinkage Algorithm Object



    """

    def __init__(self, arg):
        super(Salsa, self).__init__()
        self.arg = arg
        self.k = 0
        self.tol = 1.0e-10
        self.maxiter = 100


        









