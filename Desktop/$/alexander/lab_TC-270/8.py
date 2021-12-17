

from numpy import array, arange
from math import sin, pi
import matplotlib.pyplot as plt
import random

def f():
	amplitude=random.uniform(1,10)
	sin_sig = array([amplitude*sin((2.*pi/256)*t) for t in range(256)])
	plt.plot(arange(0,1,1.0/256), sin_sig, 'r')
	plt.xlabel('t')
	plt.ylabel('f')
	plt.show()
	return amplitude*0.637

print (f())
