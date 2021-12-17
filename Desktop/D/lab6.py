# -*- coding: utf-8 -*-
import math
import matplotlib.pyplot as plt
from matplotlib import cm
from scipy import signal
from scipy.fft import fft, ifft, fftfreq
import numpy as np
import random
import soundfile as sf


def make_imp_signal(x, a, imp_pos, imp_length):
    res = []
    for t in x:
        if t<imp_pos:
            res.append(0)
        elif t<=imp_pos+imp_length:
            res.append(a)
        else:
            res.append(0)
    return res;

def make_random_signal(x, a):
    res = []
    for t in x:
        res.append(random.uniform(a, -a))
    return res;

def show_fun_fft(x, y):
    plt.subplot(2,1,1)
    plt.plot(x, y)
    plt.subplot(2,1,2)
    xx = np.arange(len(x)/2)
    plt.stem(xx/x[-1], (abs(fft(y))/(len(x)))[:len(xx)])
    plt.show()

def signal_noise(x, y):
    As = np.std(x)
    An = np.std(y)
    return 20.0*np.log10(As/An)

#----------1

FD = 128
T = 5.0
A = 1.0
t = np.arange(0.0, T, 1.0/FD)
orig = np.array(make_imp_signal(t, A, 3.0, 0.1))
noise = np.array(make_random_signal(t, 0.5))
sig = orig+noise;
a, b = signal.butter(8, 10/(FD/2), 'low')
z = signal.lfilter(a, b, sig)

plt.plot(t, sig, label="original")
plt.plot(t, z, label="low Buttervord order 8")
plt.legend()
plt.show()
print("1")
print("before: "+str(signal_noise(orig, sig)) + "dB")
print("after : "+str(signal_noise(orig, z))+ "dB")


#---------2
FD = 128
T = 1.0
A = 1.0
t = np.arange(0.0, T, 1.0/FD)
orig = A*np.sin(2.0*np.pi*10.0*t)
noise = np.array(make_random_signal(t, 2.0))
sig = orig+noise;
N, Wn = signal.cheb1ord(10/(FD/2), 15/(FD/2), 3, 40)
#print (N, Wn)
a, b = signal.cheby1(N, 3, Wn, 'low')
z = signal.lfilter(a, b, sig)

N1, Wn1 = signal.cheb1ord(15/(FD/2), 10/(FD/2), 3, 40)
#print (N1, Wn1)
a1, b1 = signal.cheby1(N1, 3, Wn1, 'high')
z1 = signal.lfilter(a1, b1, sig)

N2, Wn2 = signal.cheb1ord([5/(FD/2),15/(FD/2)], [3/(FD/2), 17/(FD/2)], 3, 30)
#print (N2, Wn2)
a2, b2 = signal.cheby1(N2, 3, Wn2, 'bp')
z2 = signal.lfilter(a2, b2, sig)

plt.plot(t, sig, label="original")
plt.plot(t, z, label="low Chebishev1 order 6")
plt.plot(t, z1, label="high Chebishev1 order 6")
plt.plot(t, z2, label="bandpass Chebishev1 order 6")
plt.legend()
plt.show()
print("2")
print("before: "+str(signal_noise(orig, sig)) + "dB")
print("after (low 6): "+str(signal_noise(orig, z))+ "dB")
print("after (high 6): "+str(signal_noise(orig, z1))+ "dB")
print("after (bandpass 6): "+str(signal_noise(orig, z2))+ "dB")

#------3
FD = 128
T = 10.0
A = 1.0
t = np.arange(0.0, T, 1.0/FD)
orig = np.array(make_random_signal(t, 0.01))
noise = A*np.sin(2.0*np.pi*50.0*t)
sig = orig+noise;
N, Wn = signal.buttord([49/(FD/2), 51/(FD/2)], [49.5/(FD/2), 50.5/(FD/2)], 3, 30)
print(N, Wn)
a, b = signal.butter(N, Wn, 'bs')
z = signal.lfilter(a, b, sig)

plt.subplot(3,1,1)
plt.plot(t, orig, label="original")
plt.legend()
plt.subplot(3,1,2)
plt.plot(t, sig, label="noised")
plt.legend()
plt.subplot(3,1,3)
plt.plot(t, z, label="filtered")
plt.legend()
plt.show()

#show_fun_fft(t, orig)
#show_fun_fft(t, z)

print("3")
print("before: "+str(signal_noise(orig, sig)) + "dB")
print("after : "+str(signal_noise(orig, z))+ "dB")

#-------------4
t = np.arange(0.0, )
sig, FD = sf.read('gs-16b-1c-44100hz.wav')
t = np.arange(0.0, 0.1, 1/FD)
show_fun_fft(t, sig[:len(t)])

#print(len(data))
N, Wn = signal.buttord(450/(FD/2), 480/(FD/2), 3, 7)
print (N, Wn)
a, b = signal.butter(N, Wn, 'low')
z = signal.lfilter(a, b, sig)

show_fun_fft(t, z[:len(t)])


N1, Wn1 = signal.buttord([450/(FD/2),1000/(FD/2)], [400/(FD/2), 1050/(FD/2)], 3, 7)
print (N1, Wn1)
a1, b1 = signal.butter(N1,Wn1, 'bp')
z1 = signal.lfilter(a1, b1, sig)

show_fun_fft(t, z1[:len(t)])


N2, Wn2 = signal.buttord([1000/(FD/2),4000/(FD/2)], [800/(FD/2), 4200/(FD/2)], 3, 9)
print (N2, Wn2)
a2, b2 = signal.butter(N2, Wn2, 'bp')
z2 = signal.lfilter(a2, b2, sig)

show_fun_fft(t, z1[:len(t)])

sf.write("1.wav", z, FD)
sf.write("2.wav", z1, FD)
sf.write("3.wav", z2, FD)
