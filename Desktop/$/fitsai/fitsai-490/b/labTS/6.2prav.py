#!/usr/bin/env python
#coding=utf8

from numpy import array, arange, abs as np_abs
from math import sin, pi
import matplotlib.pyplot as plt
import matplotlib as mpl
import random
import numpy as np
from matplotlib import rc

rc('text', usetex=True)
rc('text.latex',unicode=True)
rc('text.latex',preamble='\usepackage[utf8]{inputenc}')
rc('text.latex',preamble='\usepackage[russian]{babel}')

def sqwave(p,X,T,aa,A,fd):
    x = []
    r = np.arange(p,X,1.0/fd)
    taue = aa+T
    x00 = r[(np.abs(r - aa)).argmin()]
    x01 = r[(np.abs(r - taue)).argmin()]
    if aa+T > X:
        return 1
    for i in r:
        if i >= x00 and i <= x01:
            x.append(A)
        else:
            x.append(0.0)
    return [r, x]

print('Input duration of impuls:')
duration = float(input())
print('Enter Amplitude:')
Amp = float(input())
a = sqwave(0, 10, duration, np.random.rand(1) * 10.0, Amp, 256.0)
while a == 1:
    a = sqwave(0, 10, duration, np.random.rand(1) * 10.0, Amp, 256.0)
plt.plot(a[0], a[1], 'm')
plt.title(u'Прямокутний iмпульс')
plt.ylabel(u'Амплiтуда')
plt.xlabel(u'Час, с')
plt.grid(True)
axes = plt.gca()
axes.set_xlim([-1,11])
axes.set_ylim([-1,Amp+2.0])
plt.show()
