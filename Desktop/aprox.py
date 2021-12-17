import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import csv

def tr(m, index):
    res = []
    for row in m:
        res.append(row[index])
    return res

with open("vax_vx.csv") as f:
    data = [list(map(float, row)) for row in csv.reader(f, delimiter=';')]

x = data[0]
y = data[1]
# errorbar expects array of shape 2xN and not Nx2 (N = len(x)) for xerr and yerr
#xe = data[:, 2:3].T
#ye= data[:, 7:8].T

plt.errorbar(tr(data, 0), tr(data, 1), xerr=tr(data, 2), yerr=tr(data, 3), fmt=".-")
plt.show()
