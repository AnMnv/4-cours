#!/usr/bin/env python
#coding=utf8
import matplotlib.pyplot as plt
import numpy as np

fig ,axs = plt.subplots(2,2)
ax0, ax1, ax2, ax3 = axs.flatten()

a = np.random.standard_exponential(500)
b = np.random.standard_cauchy(500)
c = np.random.normal(size = 500)
d = np.random.laplace(size = 500)


axs[0,0].hist(a, density=True, bins=200, color = "black")
ax0.set_title('Exponential distribution')

axs[0,1].hist(b, density=True, bins=100, color = "red")
ax1.set_title('Cauchy distribution')

axs[1,0].hist(c, density=True, bins=200, color = "blue")
ax2.set_title('Normal distribution')

axs[1,1].hist(d, density=True, bins=200, color = "brown")
ax3.set_title('Laplace distribution')

plt.suptitle("Histograms of random numbers with different probability density distributions")

plt.show()
