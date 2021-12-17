#!/usr/bin/env python
#coding=utf8
from numpy import array, arange, abs as np_abs
from math import sin, pi
import matplotlib.pyplot as plt
import matplotlib as mpl
import random
from matplotlib import rc

rc('text', usetex=True)
rc('text.latex',unicode=True)
rc('text.latex',preamble='\usepackage[utf8]{inputenc}')
rc('text.latex',preamble='\usepackage[russian]{babel}')

fd = 256.
t_minimum = -1.
t_maximum = 101.
delta_t = 1.0/fd;
print ('Амплитуда: ')
A = input()
print ('Ширина from 1 up to 10 : ')
b = input()
print ('Відстань між імпульсами: ')
a = input()
if b>10:
	print (u'Iмпульс за графiком!!!!!!!!!!')
	exit()
def qwe(x,imp_n,imp_d):
    if x < imp_n:
        return 0;
    if x < imp_n+imp_d:
        return A;
    return 0;



x = [];
y = [];
t = t_minimum;
while t<=t_maximum:
    k = t
    l = t + a + b
    m = t+a
    while k<=l:
        x.append(t);
        y.append(qwe(t,m,b));
        k += delta_t
        t += delta_t

plt.subplot(2,1,1)
plt.plot(x, y, 'k')
plt.title(u'Рандомна відстань')
plt.xlabel('Time, s')
plt.ylabel('Amplitude')
plt.grid(True)
axes = plt.gca()
axes.set_xlim([-1,101])
axes.set_ylim([-1,A+1])
plt.hold(True)


x1 = [];
y1 = [];
t = t_minimum;
while t<=t_maximum:
    k = t
    o = random.uniform(1,10)
    l = t + o + b
    m = t+o
    while k<=l:
        x1.append(t);
        y1.append(qwe(t,m,b));
        k += delta_t
        t += delta_t

plt.subplot(2,1,2)
plt.plot(x1, y1, 'm')
plt.title(u'Рандомна відстань')
plt.xlabel('Time, s')
plt.ylabel('Amplitude')
plt.grid(True)
axes = plt.gca()
axes.set_xlim([-1,101])
axes.set_ylim([-1,A+1])
plt.hold(True)
plt.show()
