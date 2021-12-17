#!/usr/bin/env python
#coding=utf8

from numpy import array, arange, abs as np_abs

from math import sin, pi
import matplotlib.pyplot as plt
import random
from matplotlib import rc
rc('text', usetex=True)
rc('text.latex',unicode=True)
rc('text.latex',preamble='\usepackage[utf8]{inputenc}')
rc('text.latex',preamble='\usepackage[russian]{babel}')

def qwe():
f=1.
	fd = 256
	n = 256
	W=(2.*pi*f/fd)
	Amplitude=random.uniform(1,10)

	signal = array([Amplitude*sin(W*q) for q in range(n)])
	plt.plot(arange(n)/float(fd), signal, 'b')
	plt.xlabel('Time, s')
	plt.ylabel('Amplitude = '+  str(Amplitude))
	plt.title(u'Синусоїдальний сигнал, з частотою  ' +  str((f)))
	plt.grid(True)
	plt.hold(True)
	plt.show()
	return A*0.637

print (qwe())
