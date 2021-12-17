#!/usr/bin/env python
#coding=utf8

from numpy import array, arange, abs as np_abs
from math import sin, pi
import matplotlib.pyplot as plt
import random

def f():
	fd = 256
	n = 256
	w=(2.0*pi/fd)
	A=random.uniform(1,10)
	plt.plot(arange(n)/float(fd), array([A*sin(w*t) for t in range(n)]))
	plt.xlabel('Time, s')
	plt.ylabel('Amplitude = '+  str(A))
	plt.title('Sin signal')
	plt.grid(True)
	plt.hold(True)
	plt.show()
	return A*0.637

print (f())
