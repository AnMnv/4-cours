#!/usr/bin/env python
#coding=utf8
#*********************************************
from numpy import array, arange, abs as np_abs
from math import sin, pi
import matplotlib.pyplot as plt
import matplotlib as mpl
import random

dfr = 256
dlinna = 256
fr=1.
ampl=random.uniform(1,10)
W=2.*pi*fr/dfr

signal = array([ampl*sin(W*a) for a in range(dlinna)])
plt.plot(arange(dlinna)/float(dfr), signal, 'b')
plt.xlabel('Time, s')
plt.ylabel('Applitude')
plt.grid(True)
plt.show()