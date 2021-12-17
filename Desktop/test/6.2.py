#!/usr/bin/env python
#coding=utf8
from numpy import array, arange, abs as np_abs

from math import sin, pi
import matplotlib.pyplot as plt
import matplotlib as mpl
import random
mpl.rcParams['font.family'] = 'fantasy'
mpl.rcParams['font.fantasy'] = 'Comic Sans MS, Arial'
import numpy as np

fd = 256.0
t_min = -0.5
t_max = 10.5
delta_t = 1.0/fd;
print ('Ведите Амплитуду: ')
A = input()
print ('Ведите Ширину Импульса((0;10]): ')
b = input()
a = random.uniform(0,10-b)
if b>10:
	print ("Iмпульс за межами графіка")
	exit()
def f(x):
    if x < a:
        return 0;
    if x < a+b:
        return A;
    return 0;


x = [];
y = [];
t = t_min;
while t<=t_max:
    x.append(t);
    y.append(f(t));
    t += delta_t

np.savez('example_2', x, y, A)
plt.plot(x, y, 'r')
plt.xlabel('time, s')
plt.ylabel('Applitude')
plt.title('square wave')
plt.grid(True)
axes = plt.gca()
axes.set_xlim([-1,11])
axes.set_ylim([-1,A+1])
plt.show()