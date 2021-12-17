# !/usr/bin/env python
# coding=utf8

import numpy as np
import matplotlib.pyplot as plt

import scipy.signal as sig

b = [2, -3, -1, 7, 4]
a = [1, 2, -2, 6, 0]
df = 1000

w, h = sig.freqz(b, a, fs=df*2*np.pi)

f = w/2/np.pi
H = abs(h)

plt.xlabel('Гц')
plt.plot(f, H, 'm')
plt.grid()
plt.show()
