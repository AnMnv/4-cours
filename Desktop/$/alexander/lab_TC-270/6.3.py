
from numpy import array, arange
import matplotlib.pyplot as plt
import random

amplituda = float(input())
dlitelnost = float(input())
start = float(input())
if dlitelnost>10:
    print ("oshibka")
    exit()

t = arange(0, 100, 1.0/256)
f = array([0 for i in t])
i = 0;
impuls = start;
while i<len(t):
    if t[i] >= impuls and t[i] <= impuls+dlitelnost:
        f[i] = amplituda
    elif t[i] > impuls+dlitelnost:
        impuls += dlitelnost+start;
    i+=1;

plt.subplot(2,1,1)
plt.plot(t, f, 'r')
plt.xlabel('t')
plt.ylabel('f')
plt.hold(True)

t = arange(0, 100, 1.0/256)
f = array([0 for i in t])
i = 0;
impuls = random.uniform(1,5)
while i<len(t):
    if t[i] >= impuls and t[i] <= impuls+dlitelnost:
        f[i] = amplituda
    elif t[i] > impuls+dlitelnost:
        impuls += dlitelnost+random.uniform(1,5)
    i+=1;

plt.subplot(2,1,2)
plt.plot(t, f, 'r')
plt.xlabel('t')
plt.ylabel('f')
plt.hold(True)

plt.show()
