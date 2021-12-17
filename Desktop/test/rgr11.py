#!/usr/bin/env python
# coding=utf8

import matplotlib.cm as cm
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

accuracy = 0.01
V1 = -3.
V2 = -0.5
delta = 0.1
xmax = 6
ymax = 3
xset = int(xmax/delta)
yset = int(ymax/delta)
points_in_mkm = int(1.0/delta)

def max_delta (mas1, mas2):
    res = 0.
    for i in np.arange(yset+1):
        for j in np.arange(xset+1):
            if math.fabs(mas1[i][j] - mas2[i][j]) > res:
                res = math.fabs(mas1[i][j] - mas2[i][j])
    return res

a = np.zeros((int(yset+1), int(xset+1)))
for i in range(xset+1):
    a[0][i] = V1
#для затвора
for i in range(points_in_mkm, 2*points_in_mkm+1):
    a[2*points_in_mkm][i] = V2
    a[2*points_in_mkm][i+3*points_in_mkm] = V2
while True:
    b = np.copy(a)
    for i in np.arange(1,yset):
        for j in np.arange(xset+1):
            if i  == 2*points_in_mkm and (j in range(points_in_mkm, 2*points_in_mkm+1) or j in range(4*points_in_mkm,5*points_in_mkm+1)):
                continue
            elif j == 0:
                a[i][j] = a[i][j+1]
            elif j == xset:
                a[i][j] = a[i][j-1]
            else:
                 a[i][j] = (a[i+1][j] + a[i][j+1] + a[i-1][j] + a[i][j-1])/4
    eps = max_delta(a,b)
    print (eps)
    if eps < accuracy:
        break
print (a)

Ex = np.zeros((yset+1, xset+1))
Ey = np.zeros((yset+1, xset+1))

for i in np.arange(yset+1):
    for j in np.arange(xset+1):
        if i == 0 and j == 0:
            Ex[i][j] = a[i][j] - a[i+1][j]
            Ey[i][j] = a[i][j] - a[i][j+1]
        elif i == 0 and j == xset:
            Ex[i][j] = a[i][j] - a[i+1][j]
            Ey[i][j] = a[i][j-1] - a[i][j]
        elif i == yset and j == 0:
            Ex[i][j] = a[i-1][j] - a[i][j]
            Ey[i][j] = a[i][j] - a[i][j+1]
        elif i == yset and j == xset:
            Ex[i][j] = a[i-1][j] + a[i][j]
            Ey[i][j] = a[i][j-1] + a[i][j]
        elif i == 0:
            Ex[i][j] = a[i][j] - a[i+1][j]
            Ey[i][j] = a[i][j-1] - a[i][j+1]
        elif i == yset:
            Ex[i][j] = a[i-1][j] - a[i][j]
            Ey[i][j] = a[i][j-1] - a[i][j+1]
        elif j == 0:
            Ex[i][j] = a[i-1][j] - a[i+1][j]
            Ey[i][j] = a[i][j] - a[i][j+1]
        elif j == xset:
            Ex[i][j] = a[i-1][j] - a[i+1][j]
            Ey[i][j] = a[i][j-1] - a[i][j]
        else:
             Ex[i][j] = a[i-1][j] - a[i+1][j]
             Ey[i][j] = a[i][j-1] - a[i][j+1]


print (a)
print ('###################')
print(Ex)
print(Ey)

X = []
Y = []

for i in np.arange(yset+1):
    xline = []
    yline = []
    for j in np.arange(xset+1):
        xline.append(delta*j)
        yline.append(delta*i)
    X.append(xline)
    Y.append(yline)

U = Ex
V = Ey


widths = np.linspace(0, 1, V.size)
w = 0.004
plt.quiver(X, Y, V, U, width = w)
plt.title('Tension vectors in every point of space ')
axes = plt.gca()
axes.set_xlim([-0.1,6.1])
axes.set_ylim([-0.1,3.1])
plt.show()

fig, ax = plt.subplots()
CS = ax.contour(X, Y, a, levels = np.arange(-1, 3, 0.2))
ax.clabel(CS, inline=True, fontsize=10)
ax.set_title('Equipotential lines')
ax.set_xlim([-0.1,6.1])
ax.set_ylim([-0.1,3.1])
plt.show()

fig = plt.figure()
ax = fig.gca(projection='3d')
CS = ax.plot_surface(X, Y, a, cmap = cm.coolwarm)
ax.contour(X, Y, a, zdir='z', offset=-0.7, levels = np.arange(-1, 3, 0.2))
ax.clabel(CS, inline=True, fontsize=10)
ax.set_title('Equipotential surface')
ax.set_xlim([-0.1,6.1])
ax.set_ylim([-0.1,3.1])
plt.show()
