
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from numpy import array, arange, abs as np_abs
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc

rc('text', usetex=True)
rc('text.latex',unicode=True)
rc('text.latex',preamble= '\usepackage[utf8]{inputenc}')
rc('text.latex',preamble= '\usepackage[russian]{babel}')

mas = [i for i in range(150)]#massive
print(mas)

fig ,axs = plt.subplots(2,2)
ax0, ax1, ax2, ax3 = axs.flatten()

a = np.random.standard_exponential(500)
b = np.random.standard_cauchy(100)
c = np.random.normal(size = 600)
d = np.random.laplace(size = 700)


axs[0,0].hist(a, bins=200)
ax0.set_title(u'Экспоненциальное распределение' )
axs[0,1].hist(b, bins=100)
ax1.set_title(u'Распределение Коши')
axs[1,0].hist(c, bins=200)
ax2.set_title(u'Нормальное распределение')
axs[1,1].hist(d, bins=200)
ax3.set_title(u'Распределение Лапласа')
plt.show()
