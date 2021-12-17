#!/usr/bin/env python
#coding=utf8
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 10, 0.05)
y = 4*x + 2
plt.title("Linear dependence y = 4*x + 2")
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.plot(x, y, "k")
plt.show()
