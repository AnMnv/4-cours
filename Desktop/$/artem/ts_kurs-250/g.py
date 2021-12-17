# !/usr/bin/env python
# coding=utf8

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

a = [1, 4, -2, 3, 0]
b = [5, -2, -4, 4, 5]
df = 1000

w, h = sig.freqz(b, a, fs=df*2*np.pi)

f = w/2/np.pi
H = abs(h)

plt.xlabel('Гц')
plt.plot(f, H)
plt.grid()
plt.show()
