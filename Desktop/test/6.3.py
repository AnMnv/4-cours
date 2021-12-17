#!/usr/bin/env python
#coding=utf8
from numpy import array, arange, abs as np_abs

from math import sin, pi
import matplotlib.pyplot as plt
import matplotlib as mpl
import random
mpl.rcParams['font.family'] = 'fantasy'
mpl.rcParams['font.fantasy'] = 'Comic Sans MS, Arial'

fd = 256.0
t_min = -0.5
t_max = 100.5
delta_t = 1.0/fd;
print ('Ведите aмплитуду: ')
A = input()
print ('Введіть ширину импульса( (0;10] ): ')
b = input()
print ('Введіть інтервали між імпульсами: ')
a = input()
#a = random.uniform(0,10-b)
if b>10:
	print ("Iмпульс за межами графіка")
	exit()
def f(x,imp_begin,imp_width):
    if x < imp_begin:
        return 0;
    if x < imp_begin+imp_width:
        return A;
    return 0;



x = [];
y = [];
t = t_min;
while t<=t_max:
    aa = t
    bb = t + a + b
    cc = t+a
    while aa<=bb:
        x.append(t);
        y.append(f(t,cc,b));
        aa += delta_t
        t += delta_t

x1 = [];
y1 = [];
t = t_min;
while t<=t_max:
    aa = t
    aaa = random.uniform(1,5)
    bb = t + aaa + b
    cc = t+aaa
    while aa<=bb:
        x1.append(t);
        y1.append(f(t,cc,b));
        aa += delta_t
        t += delta_t

plt.subplot(2,1,1)  
plt.plot(x, y, 'r')
plt.xlabel('time, s')
plt.ylabel('Applitude')
plt.title('square wave(intervals between pulses are the same)')
plt.grid(True)
axes = plt.gca()
axes.set_xlim([-1,101])
axes.set_ylim([-1,A+1])
plt.hold(True)



plt.subplot(2,1,2)  
plt.plot(x1, y1, 'g')
plt.xlabel('time, s')
plt.ylabel('Applitude')
plt.title('square wave(intervals between pulses are random)')
plt.grid(True)
axes = plt.gca()
axes.set_xlim([-1,101])
axes.set_ylim([-1,A+1])
plt.hold(True)
plt.show()






