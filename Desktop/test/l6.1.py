#!/usr/bin/env python
#coding=utf8

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,AutoMinorLocator)
import matplotlib.pyplot as mp
import random
from scipy import signal

fig,ax=plt.subplots()

plt.grid()#координатная сетка
plt.xlabel("t, s") # ось абсцисс
plt.ylabel("f(t), V") # ось ординат
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.tick_params(which='major', length=10, width=2)
ax.tick_params(which='minor', length=5, width=1)

ax.grid(which="major", linewidth=1.2)
ax.grid(which="minor", linestyle="+", color="gray", linewidth=0.5)

t0 = 0
t10 = 10
delta_t = 1.0/256.0#  1 / частоту дискретизации
Amplitude = 5
b = 1.
a = 4.0 - b/2;

def function(x_depend):
    if x_depend < a:
        return 0;
    if x_depend < a+b:
        return Amplitude;
    return 0;

x = [];
y = [];
time_po_osi_x = t0;
while time_po_osi_x<=t10:
    x.append(time_po_osi_x);
    y.append(function(time_po_osi_x));
    time_po_osi_x += delta_t


axes = plt.gca()
axes.set_xlim([-1,11])
axes.set_ylim([-1,6])
plt.plot(x,y,'g')




plt.show()
