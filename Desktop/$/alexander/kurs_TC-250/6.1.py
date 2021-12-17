
from numpy import array, arange, abs as np_abs
import matplotlib.pyplot as plt

def func(x, start, dlitelnost):
    if x < start:
        return 0;
    if x < start+dlitelnost:
        return 5;
    return 0;

t = arange(0, 10, 1.0/256);
f = array([func(i, 4.0 - 0.3/2, 0.3) for i in t])

plt.plot(t, f, 'r')
plt.xlabel('vremja, s')
plt.ylabel('amplituda')
plt.show()
