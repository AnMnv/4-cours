
from numpy import array, arange, abs as np_abs
import json
from math import sin, pi
import matplotlib.pyplot as plt
import matplotlib as mpl
import random
from matplotlib import rc

rc('text', usetex=True)
rc('text.latex',unicode=True)
rc('text.latex',preamble='\usepackage[utf8]{inputenc}')
rc('text.latex',preamble='\usepackage[russian]{babel}')


fd = 256.0
tmin = -0.5
tmax = 100.5
delta_t = 1.0/fd;
print ('A: ')
A = input()
print ('Ширина от 1 до 10: ')
b = input()
print ('Интервалы между импульсами: ')
a = input()
if b>10:
    print ("Импульс вылез за границы!!!")
    exit()

def f(x,imp_begin,imp_width):
    if x > imp_begin and x < imp_begin+imp_width:
        return A;
    return 0;

def gen_a1():
    return a;

def gen_a2():
    return random.uniform(1,5);

def one(ff, position, color):
    x = [];
    y = [];
    t = tmin;
    while t<=tmax:
        aa = t
        aaa = ff();
        bb = t + aaa + b
        cc = t+a
        while aa<=bb:
            x.append(t);
            y.append(f(t,cc,b));
            aa += delta_t
            t += delta_t
    plt.subplot(2,1,position)
    plt.plot(x, y, color)
    plt.xlabel(u'Час, с')
    plt.ylabel(u'Амплітуда')
    plt.grid(True)
    axes = plt.gca()
    axes.set_xlim([-1,101])
    axes.set_ylim([-1,A+1])
    plt.hold(True)
    return [x, y];

[x, y] = one(gen_a1, 1, 'k')
[x, y] = one(gen_a2, 2, 'r')
with open('data.txt', 'w') as outfile:
    json.dump({'x': x, 'y': y, 'A': A}, outfile)
plt.show()
