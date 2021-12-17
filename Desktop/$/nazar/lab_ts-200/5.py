#!/usr/bin/env python
#coding=utf8

import numpy
from math import sin, pi
import matplotlib.pyplot as plt
import random

fd = 256
n = 256
a=random.uniform(1,10)

def get_plot_arrays(fd, n, f):
    w=(2.*pi*f/fd)
    A=random.uniform(1,10)
    return [numpy.arange(n)/float(fd), numpy.array([a*sin(w*t) for t in range(n)])]

def show(data, pos, title, color = 'm'):
    plt.subplot(3,1,pos)
    plt.plot(data[0], data[1], color)
    plt.xlabel('Time, s')
    plt.ylabel('Amplitude = '+  str(a))
    plt.title(title)
    plt.grid(True)
    plt.hold(True)

show(get_plot_arrays(fd, n, 1), 1, 'Sin signal, Frequency = ' +  str("{0:.0f}".format(1) )+' Hz')
show(get_plot_arrays(fd, n, 10), 2, 'Sin signal, Frequency = ' +  str("{0:.0f}".format(10) )+' Hz')
show(get_plot_arrays(fd, n, 50), 3, 'Sin signal, Frequency = ' +  str("{0:.0f}".format(50) )+' Hz')

plt.show()
