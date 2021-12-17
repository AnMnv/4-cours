#!/usr/bin/env python
#coding=utf8

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np


mas = [i for i in range(50)]
print(mas)

fig ,axs = plt.subplots(2,2)

a = np.random.standard_exponential(500)
b = np.random.standard_cauchy(100)
c = np.random.normal(size = 600)
d = np.random.laplace(size = 700)


axs[0,0].hist(a, bins=200)#Exponential distribution
axs[0,1].hist(b, bins=100)#Cauchy distribution
axs[1,0].hist(c, bins=200)#Normal distribution
axs[1,1].hist(d, bins=200)#Laplace distribution

plt.show()
