#!/usr/bin/env python
#coding=utf8
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

def imp(t_min,t_max,duration,start,A,fd):
    x = np.arange(t_min,t_max,1.0/fd)
    if start+duration > t_max:
        return 0;
    y = np.array([(A if (i>=start and i<=start+duration) else 0) for i in x])
    return [x, y]


print("Pulse duration: ")
duration = float(input())
print("Enter the amplitude: ")
Amp = float(input())
a = imp(0, 10, duration, np.random.rand(1) * 10.0, Amp, 256.0)
while a == 0:
    a = imp(0, 10, duration, np.random.rand(1) * 10.0, Amp, 256.0)
plt.plot(a[0], a[1], 'g')
plt.title("Square wave")
plt.xlabel("Time, s")
plt.ylabel("Amplitude")
plt.grid(False)
plt.show()
