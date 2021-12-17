#!/usr/bin/env python
#coding=utf8
from pylab import figure, axes, pie, title, show
import matplotlib.cm as cm
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math


accuracy = 0.01
e = -1.6*10**(-19)
V1 = 5.0
V2 = -1.0
ah = 0.25
xmax = 6
ymax = 3
xset = int(xmax/ah)
yset = int(ymax/ah)
points_in_mkm = int(1.0/ah)

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
            Ex[i][j] = (a[i][j] - a[i+1][j])/(2*ah*10**(-6))
            Ey[i][j] = (a[i][j] - a[i][j+1])/(2*ah*10**(-6))
        elif i == 0 and j == xset:
            Ex[i][j] = (a[i][j] - a[i+1][j])/(2*ah*10**(-6))
            Ey[i][j] = (a[i][j-1] - a[i][j])/(2*ah*10**(-6))
        elif i == yset and j == 0:
            Ex[i][j] = (a[i-1][j] - a[i][j])/(2*ah*10**(-6))
            Ey[i][j] = (a[i][j] - a[i][j+1])/(2*ah*10**(-6))
        elif i == yset and j == xset:
            Ex[i][j] = (a[i-1][j] + a[i][j])/(2*ah*10**(-6))
            Ey[i][j] = (a[i][j-1] + a[i][j])/(2*ah*10**(-6))
        elif i == 0:
            Ex[i][j] = (a[i][j] - a[i+1][j])/(2*ah*10**(-6))
            Ey[i][j] = (a[i][j-1] - a[i][j+1])/(2*ah*10**(-6))
        elif i == yset:
            Ex[i][j] = (a[i-1][j] - a[i][j])/(2*ah*10**(-6))
            Ey[i][j] = (a[i][j-1] - a[i][j+1])/(2*ah*10**(-6))
        elif j == 0:
            Ex[i][j] = (a[i-1][j] - a[i+1][j])/(2*ah*10**(-6))
            Ey[i][j] = (a[i][j] - a[i][j+1])/(2*ah*10**(-6))
        elif j == xset:
            Ex[i][j] = (a[i-1][j] - a[i+1][j])/(2*ah*10**(-6))
            Ey[i][j] = (a[i][j-1] - a[i][j])/(2*ah*10**(-6))
        else:
             Ex[i][j] = (a[i-1][j] - a[i+1][j])/(2*ah*10**(-6))
             Ey[i][j] = (a[i][j-1] - a[i][j+1])/(2*ah*10**(-6))
print(Ex[2][1], Ey[2][1])

#print (a)
print ('###################')
print(Ex)
print(Ey)

X = []
Y = []

for i in np.arange(yset+1):
    xline = []
    yline = []
    for j in np.arange(xset+1):
        xline.append(ah*j)
        yline.append(ah*i)
    X.append(xline)
    Y.append(yline)

U = Ex
V = Ey

fig, ax = plt.subplots()
widths = np.linspace(0, 1, V.size)
w = 0.003
plt.quiver(X, Y, V, U, width = w)
axes = plt.gca()
axes.set_xlim([-0.1,6.1])
axes.set_ylim([-0.1,3.1])
fig.savefig('/Users/antonmnacakanov/Desktop/11.pdf', dpi=1000)
plt.close(fig)

fig, ax = plt.subplots()
CS = ax.contour(X, Y, a, levels = np.arange(-1, 5, 0.3))
ax.clabel(CS, inline=True, fontsize=10)
ax.set_xlim([-0.1,6.1])
ax.set_ylim([-0.1,3.1])
fig.savefig('/Users/antonmnacakanov/Desktop/21.pdf', dpi=1000)
plt.close(fig)

fig = plt.figure()
ax = fig.gca(projection='3d')
CS = ax.plot_surface(X, Y, a, cmap = cm.plasma)
ax.contour(X, Y, a, zdir='z', offset=-1.0, levels = np.arange(-1, 5, 0.3))
ax.clabel(CS, inline=True, fontsize=10)
ax.set_xlim([-0.1,6.1])
ax.set_ylim([-0.1,3.1])
fig.savefig('/Users/antonmnacakanov/Desktop/31.pdf', dpi=1000)
plt.close(fig)

f = open("/Users/antonmnacakanov/Desktop/data.csv", "w")
for j in np.arange(xset+1):
    f.write(str(j)+";")
f.write('\n')
for i in np.arange(yset+1):
    for j in np.arange(xset+1):
        f.write(str(round(a[i][j],3))+";")
    f.write('\n')
f.close()

for i in np.arange(yset+1):
    for j in np.arange(xset+1):
        a[i][j] = e * a[i][j];
fig = plt.figure()
ax = fig.gca(projection='3d')
CS = ax.plot_surface(X, Y, a, cmap = cm.plasma)
ax.contour(X, Y, a, zdir='z', offset=-8.0*10**(-19), levels = np.arange(-5*10**(-19),5*10**(-19), 0.3*10**(-19)))
ax.clabel(CS, inline=True, fontsize=10)
ax.set_xlim([-0.1,6.1])
ax.set_ylim([-0.1,3.1])
fig.savefig('/Users/antonmnacakanov/Desktop/3.11.pdf', dpi=1000)
plt.close(fig)
