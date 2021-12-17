

from numpy import array, arange, abs as np_abs
from math import sin, pi
import matplotlib.pyplot as plt
import random
from matplotlib import rc

rc('text', usetex=True)
rc('text.latex',unicode=True)
rc('text.latex',preamble='\usepackage[utf8]{inputenc}')
rc('text.latex',preamble='\usepackage[russian]{babel}')

def f():
	fd = 256.
	b = 256.0
	F=1.0
	w=(2.*pi*F/fd)
	Amp=random.uniform(1,10)
	signal = array([Amp*sin(w*t) for t in arange(b)])
	plt.plot(arange(b)/float(fd), signal, 'k')
	plt.xlabel(u'Час, с')
	plt.ylabel(u'Амплітуда')
	plt.grid(True)
	plt.show()
	return Amp*0.637

print (f())
