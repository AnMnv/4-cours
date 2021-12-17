from math import pi, log, sin, cos, tan
import matplotlib.pyplot as plt
from numpy import array, arange, sqrt, abs as np_abs

D = 0.41  # mm
d = 2.2  # mm
f = 2*10**9
E = 2.2
E0 = (10**(-9))/(36*pi)
c = 3*10**8


mu = 1.0
mu0 = 4.0*pi*10.0**(-7)  # (Гн/м)
Z0 = sqrt((mu*mu0*log(0.0073/0.0012)**2)/(4*pi**2*E*E0))
print("Z_0 = ", Z0, "Ом")
k = (2*pi*f*sqrt(E))/(c)
print("k = ", k)
L = 1/(2*pi*f*12.3)
print("L = ", L)
lh = (2*pi*L)/(mu*mu0*log(0.0073/0.0012))
print("l = ", lh)

X = arange(0.0, 1, 0.0001)
Ux = []
Ix = []
for i in X:
    Ux.append(sqrt(1.0+0.82*cos(62.0*i-1.5)+0.1681))
    Ix.append(sqrt(1.0-0.82*cos(62.0*i-1.5)+0.1681))

Xre = arange(0.0, 0.1, 0.0001)
re = []
im = []
flag = False
for i in Xre:
    im.append(103*(-5000.0*tan(31.0*i)-(50*73)+73*73*tan(31.0*i)+73*50*((tan(31.0*i))**2))/((73+50*tan(31*i))**2+(50*tan(31*i))**2))
    re.append(103*(73*50*tan(31.0*i)+(5000*tan(31.0*i))+73*50*(tan(31.0*i))**2)/((73+50*tan(31*i))**2+(50*tan(31*i))**2))
    if re[-1] > 73 and not flag:
        print(i)
        print(im[-1])
        flag = True

fig, ax = plt.subplots()
ax.axhline(y=0, linestyle=':', color='g')
ax.axhline(y=1.41, linestyle='--', color='m')
ax.axhline(y=0.59, linestyle='--', color='m')
ax.axvline(x=0, linestyle=':', color='g')
plt.plot(X, Ux, label='Vm(x)/V')
plt.plot(X, Ix, label='Im(x)/I')
plt.grid()
plt.xlabel("x, м")
plt.ylabel("Нормована амплітуда")
plt.legend()
plt.savefig('c:/Users/anmnm/Desktop/1.pdf')

fig, ax = plt.subplots()
plt.scatter(0.0262, 73)
plt.scatter(0.0262, 4.211, c = 'orange')
plt.plot(Xre, re, label='ReZ(x)')
plt.plot(Xre, im, label='ImZ(x)', c = 'orange')
plt.grid()
plt.xlabel("x, м")
plt.ylabel("Z, Ом")
plt.legend()
plt.savefig('c:/Users/anmnm/Desktop/2.pdf')
