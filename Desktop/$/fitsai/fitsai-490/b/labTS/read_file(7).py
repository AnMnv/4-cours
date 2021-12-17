#!/usr/bin/env python
#coding=utf8
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

rc('text', usetex=True)
rc('text.latex',unicode=True)
rc('text.latex',preamble='\usepackage[utf8]{inputenc}')
rc('text.latex',preamble='\usepackage[russian]{babel}')

ex_2 = np.load('SAVE.npz')
ex_2.files
x = ex_2['arr_0']
y = ex_2['arr_1']
Amplitude = ex_2['arr_2']

plt.plot(x, y, Amplitude, 'k')
plt.title(u'Прямокутний iмпульс прочитаний з файлу SAVE.npz')
plt.xlabel('Time, s')
plt.ylabel('Amplitude')
plt.grid(True)
axes = plt.gca()
axes.set_xlim([-1,11])
axes.set_ylim([-1,Amplitude+1])
plt.show()
