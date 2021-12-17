

from numpy import array, arange, abs as np_abs
from math import sin, pi
import matplotlib.pyplot as plt
import matplotlib as mpl
import random
from matplotlib import rc

rc('text', usetex=True)
rc('text.latex',unicode=True)
rc('text.latex',preamble='\usepackage[utf8]{inputenc}')
rc('text.latex',preamble='\usepackage[russian]{babel}')

def one(fr, p):
    fd = 256.
    b = 256.0
    F=fr
    w=(2.*pi*F/fd)
    Amp=random.uniform(1,10)
    plt.subplot(3,1,p)
    signal = array([Amp*sin(w*t) for t in arange(b)])
    plt.plot(arange(b)/float(fd), signal, 'k')
    plt.xlabel(u'Час, с')
    plt.ylabel(u'Амплітуда')
    plt.grid(True)
    plt.hold(True)

one(1,1)
one(10,2)
one(50,3)

plt.show()
