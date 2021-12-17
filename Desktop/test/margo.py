# !/usr/bin/env python
# coding=utf8

import numpy as np
import matplotlib.pyplot as plt

import scipy.signal as sig

a = [1, 5, -2, 2, 0]
b = [6, -2, -5, 3, 5]
df = 1000

w, h = sig.freqz(b, a, fs = df*2*np.pi)

f = w/2/np.pi
H = abs(h)

plt.xlabel('Гц')
plt.plot(f, H)
plt.grid()
plt.show()
