#!/usr/bin/env python
#coding=utf8
from numpy import array, arange, abs as np_abs

import matplotlib.pyplot as plt

fd = 256.0
t_min = 0
t_max = 10
delta_t = 1.0/fd;
A = 5
duration = 0.3
begin = 4.0 - duration/2;

def f(x):
    if x < begin:
        return 0;
    if x < begin+duration:
        return A;
    return 0;

x = arange(t_min, t_max, 1.0/fd);
y = array([f(t) for t in x]);
    
plt.plot(x, y, 'r')
plt.xlabel('Time, s')
plt.ylabel('Amplitude')
plt.title('Square wave')
plt.grid(True)
axes = plt.gca()
axes.set_xlim([-1,11])
axes.set_ylim([-1,6])
plt.show()