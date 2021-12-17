#!/usr/bin/env python
#coding=utf8
#*********************************************
from numpy import array, arange, abs as np_abs

from math import sin, pi
import matplotlib.pyplot as plt
import matplotlib as mpl
import random

fr=1.
dfr = 256
dlinna = 256
ampl=random.uniform(1,10)
W=2.*pi*fr/dfr


plt.subplot(3,1,1) 
signal = array([ampl*sin(W*a) for a in range(dlinna)])
plt.plot(arange(dlinna)/float(dfr), signal, 'y')
plt.xlabel('Time, s')
plt.ylabel('Amplitude')
plt.title('Amplitude = '+  str(ampl)+' F = ' +  str(fr))
plt.grid(True)
plt.hold(True)

fr=10.
dfr = 256
dlinna = 256
ampl=random.uniform(1,10)
W=2.*pi*fr/dfr

plt.subplot(3,1,2) 
signal = array([ampl*sin(W*a) for a in range(dlinna)])
plt.plot(arange(dlinna)/float(dfr), signal, 'g')
plt.xlabel('Time, s')
plt.ylabel('Amplitude')
plt.title('Amplitude = '+  str(ampl)+' F = ' +  str(fr))
plt.grid(True)
plt.hold(True)

fr=50.
dfr = 256
dlinna = 256
ampl=random.uniform(1,10)
W=2.*pi*fr/dfr

plt.subplot(3,1,3) 
signal = array([ampl*sin(W*a) for a in range(dlinna)])
plt.plot(arange(dlinna)/float(dfr), signal, 'b')
plt.xlabel('Time, s')
plt.ylabel('Amplitude')
plt.title('Amplitude = '+  str(ampl)+' F = ' +  str(fr))
plt.grid(True)
plt.hold(True)
plt.show()