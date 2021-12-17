#!/usr/bin/env python
#coding=utf8
from numpy import array, arange, abs as np_abs

from math import sin, pi
import matplotlib.pyplot as plt
import matplotlib as mpl
import random
mpl.rcParams['font.family'] = 'fantasy'
mpl.rcParams['font.fantasy'] = 'Comic Sans MS, Arial'

FD = 256#частота дискретизации, отсчётов в секунду
N = 256#длина входного массива, N/FD секунд 
F=1.0#циклическая частота входного сигнала
w=(2.*pi*F/FD)#отсчёт круговой частоты 
A=random.uniform(1,10)#амплитуда сигнала

#сгенерируем чистый синусоидальный сигнал с частотой F длиной N
sin_sig = array([A*sin(w*t) for t in range(N)])#график сигнала
plt.plot(arange(N)/float(FD), sin_sig, 'r')
plt.xlabel('time, s')
plt.ylabel('Applitude')
plt.title('Sin signal')
plt.grid(True)
plt.show()