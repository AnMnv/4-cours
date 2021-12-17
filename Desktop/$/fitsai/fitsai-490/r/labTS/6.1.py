
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot
from matplotlib import rc

rc('text', usetex=True)
rc('text.latex',unicode=True)
rc('text.latex',preamble='\usepackage[utf8]{inputenc}')
rc('text.latex',preamble='\usepackage[russian]{babel}')

fd = 256.0
Amp = 5.0
b = 0.3
a = 4.0 - b/2;
tmin = 0
tmax = 10

data = [[],[]];
t = tmin;
while t<=tmax:
    data[0].append(t);
    if t < a:
        data[1].append(0);
    elif t < a+b:
        data[1].append(Amp);
    else:
        data[1].append(0);
    t += 1.0/fd;

matplotlib.pyplot.plot(data[0], data[1], 'orange')
plt.ylabel(u"Амплітуда")
plt.xlabel(u"Час, с")
matplotlib.pyplot.grid(True)
axes = matplotlib.pyplot.gca()
axes.set_xlim([-1,11])
axes.set_ylim([-1,Amp+0.5])
matplotlib.pyplot.show()
