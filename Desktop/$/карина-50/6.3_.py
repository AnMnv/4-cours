#!/usr/bin/env python
#coding=utf8

from math import sin, pi
import matplotlib.pyplot as plt
import matplotlib as mpl
import random

fd = 256.0
time_min = -0.5
time_max = 100.5
delta_t = 1.0/fd;
print ('Введи амплитуду: ')
A = float(input())
print ('Введи ширину импульса от 0 до 10: ')
b = float(input())
print ('Введи интервал между импульсами: ')
a = float(input())
if b>10:
    print ("Импульс за границами графика!")
    exit()

def make_imp(aa):
    data = [[], []];
    t = time_min;
    while t<=time_max:
        imp_start = t
        imp_end = imp_start + aa + b
        imp_up = t + aa
        while imp_start<=imp_end:
            data[0].append(t);
            if t < imp_up:
                data[1].append(0);
            elif t < imp_up+b:
                data[1].append(A);
            else:
                data[1].append(0);
            imp_start +=  1.0/fd;
            t += 1.0/fd;
    return data;

def make_imp1():
    data = [[], []];
    t = time_min;
    while t<=time_max:
        aa = random.uniform(1,5)
        imp_start = t
        imp_end = imp_start + aa + b
        imp_up = t + aa
        while imp_start<=imp_end:
            data[0].append(t);
            if t < imp_up:
                data[1].append(0);
            elif t < imp_up+b:
                data[1].append(A);
            else:
                data[1].append(0);
            imp_start +=  1.0/fd;
            t += 1.0/fd;
    return data;

data1 = make_imp(a);
data2 = make_imp1();

plt.subplot(2,1,1)
plt.plot(data1[0], data1[1], 'b')
plt.xlabel('Time, s')
plt.ylabel('Amplitude')
plt.title('Wave')
plt.grid(True)
axes = plt.gca()
axes.set_xlim([-1,101])
axes.set_ylim([-1,A+1])
plt.hold(True)

plt.subplot(2,1,2)
plt.plot(data2[0], data2[1], 'm')
plt.xlabel('Time, s')
plt.ylabel('Amplitude')
plt.title('Wave with random intervals')
plt.grid(True)
axes = plt.gca()
axes.set_xlim([-1,101])
axes.set_ylim([-1,A+1])
plt.hold(True)
plt.show()
