
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from matplotlib import rc

rc('text', usetex=True)
rc('text.latex',unicode=True)
rc('text.latex',preamble='\usepackage[utf8]{inputenc}')
rc('text.latex',preamble='\usepackage[russian]{babel}')

def sqwave(p,end,T,aa,A,fd):
    x = []
    r = np.arange(p,end,1.0/fd)
    taue = aa+T
    x00 = r[(np.abs(r - aa)).argmin()]
    x01 = r[(np.abs(r - taue)).argmin()]
    if aa+T > end:
        return 1
    for i in r:
        if i >= x00 and i <= x01:
            x.append(A)
        else:
            x.append(0.0)
    return [r, x]

print("Входная длительность импульса: ")
duration = float(input())
print("A: ")
Amp = float(input())
a = sqwave(0, 10, duration, np.random.rand(1) * 10.0, Amp, 256.0)
while a == 1:
    a = sqwave(0, 10, duration, np.random.rand(1) * 10.0, Amp, 256.0)
plt.plot(a[0], a[1], 'g')
plt.ylabel(u"Амплітуда")
plt.xlabel(u"Час, с")
plt.grid(True)
axes = plt.gca()
axes.set_xlim([-1,11])
axes.set_ylim([-1,Amp+1])
plt.show()
