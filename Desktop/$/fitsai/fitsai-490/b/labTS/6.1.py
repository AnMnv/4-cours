#!/usr/bin/env python
#coding=utf8
#*********************************************
from numpy import array, arange, abs as np_abs
import matplotlib.pyplot as plt
from matplotlib import rc

rc('text', usetex=True)
rc('text.latex',unicode=True)
rc('text.latex',preamble='\usepackage[utf8]{inputenc}')
rc('text.latex',preamble='\usepackage[russian]{babel}')

fd = 256.
dt = 1./fd
Amp = 5.
b = 0.3
a = 4.0 - b/2
t_minimum = 0
t_maximum = 10.

def qwe(x):
    if x < a:
        return 0
    if x < a+b:
        return Amp
    return 0

x = [];
y = [];
t = t_minimum
while t<=t_maximum:
    x.append(t)
    y.append(qwe(t))
    t += dt

axes = plt.gca()
axes.set_xlim([-1,10])
axes.set_ylim([-1,8])
plt.plot(x, y, 'k')
plt.xlabel('Time, s')
plt.ylabel('Amplitude')
plt.title(u'Прямокутний iмпульс' )
plt.grid(True)

plt.show()
