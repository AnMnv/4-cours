#!/usr/bin/env python
#coding=utf8
from numpy import array, arange
import matplotlib.pyplot as plt
import random

fd = 256.0
t_min = -0.5
t_max = 100.5
print ('Enter amplitude: ')
A = input()
print ('Enter impulse width from 0 to 10: ')
duration = input()
print ('Enter the intervals between impulses: ')
a = input()
if duration>10:
    print ("Impulse outside the schedule!")
    exit()

def f(x,imp_begin,imp_width):
    if x > imp_begin and x < imp_begin+imp_width:
        return A;
    return 0;

def gen_a1():
    return a;

def gen_a2():
    return random.uniform(1,5);

def wave(ff):
    x = arange(t_min, t_max, 1.0/fd);
    y = array([0 for i in x]);
    interval = ff();
    i = 0
    curr_imp_start = t_min;
    while i < len(x):
        if x[i]>=curr_imp_start+interval and x[i]<=curr_imp_start+interval+duration:
            y[i] = A;
        elif x[i]>curr_imp_start+interval+duration:
            curr_imp_start = x[i];
            interval = ff();
        i+=1;
    return [x, y];

def show(data, pos, color):
    plt.subplot(2,1,pos)
    plt.plot(data[0], data[1], color)
    plt.xlabel('Time, s')
    plt.ylabel('Amplitude')
    plt.grid(True)
    axes = plt.gca()
    axes.set_xlim([-1,101])
    axes.set_ylim([-1,A+1])
    plt.hold(True)

show(wave(gen_a1), 1, 'b')
plt.title('Intervals between impulses are  the same')
show(wave(gen_a2), 2, 'm')
plt.title('Intervals between impulses are not the same')

plt.show()
