

from numpy import array, arange
from math import sin, pi
import matplotlib.pyplot as plt
import random

amplituda=random.uniform(1,10)

chastota=(2.*pi*1.0/256)
amplituda=random.uniform(1,10)
plt.subplot(3,1,1)
plt.plot(arange(0,1,1.0/256), array([amplituda*sin(chastota*t) for t in range(256)]), 'r')
plt.xlabel('time')
plt.ylabel('amplitude')
plt.hold(True)

chastota=(2.*pi*10.0/256)
amplituda=random.uniform(1,10)
plt.subplot(3,1,2)
plt.plot(arange(0,1,1.0/256), array([amplituda*sin(chastota*t) for t in range(256)]), 'r')
plt.xlabel('time')
plt.ylabel('amplitude')
plt.hold(True)

chastota=(2.*pi*50.0/256)
amplituda=random.uniform(1,10)
plt.subplot(3,1,3)
plt.plot(arange(0,1,1.0/256), array([amplituda*sin(chastota*t) for t in range(256)]), 'r')
plt.xlabel('time')
plt.ylabel('amplitude')
plt.hold(True)

plt.show()
