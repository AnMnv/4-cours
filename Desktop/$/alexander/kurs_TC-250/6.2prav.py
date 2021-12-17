
import numpy as np
import matplotlib.pyplot as plt

dlitelnost = float(input())
amplituda = float(input())
start = np.random.rand(1)
while (start+dlitelnost) > 10:
    start = np.random.rand(1)

t = np.arange(0,10,1.0/256)
f = np.array([0 for i in t])
i = 0;
while i < len(t):
    if t[i] >= start and t[i] <= (start+dlitelnost):
        f[i] = amplituda
    i+=1;

plt.plot(t, f, 'g')
plt.xlabel("vremja")
plt.ylabel("amplituda")
plt.show()
