
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
fig, ax = plt.subplots()
from matplotlib import rc

rc('text', usetex=True)
rc('text.latex',unicode=True)
rc('text.latex',preamble='\usepackage[utf8]{inputenc}')
rc('text.latex',preamble='\usepackage[russian]{babel}')

x = np.linspace(1, 10, 50)
k = 10
b = 5
y = k*x + b
plt.title(u"Лінійна залежність y = kx+b")
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.plot(x, y, "m")
plt.show()
