
import matplotlib.pyplot as plt
import numpy as np

fig ,axs = plt.subplots(2,2)
ax0, ax1, ax2, ax3 = axs.flatten()

a = np.random.standard_exponential(500)
b = np.random.standard_cauchy(100)
c = np.random.normal(size = 600)
d = np.random.laplace(size = 700)


ax0.hist(a, density=True, bins=200)
ax1.hist(b, density=True, bins=100)
ax2.hist(c, density=True, bins=200)
ax3.hist(d, density=True, bins=200)

plt.show()
