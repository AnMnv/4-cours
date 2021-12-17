#!/usr/bin/env python
#coding=utf8

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

rc('text', usetex=True)
rc('text.latex',unicode=True)
rc('text.latex',preamble='\usepackage[utf8]{inputenc}')
rc('text.latex',preamble='\usepackage[russian]{babel}')

x = np.linspace(3, 5, 10)
y = 1*x
plt.title(u"Линейная функция")
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.plot(x, y, "r")
plt.show()
