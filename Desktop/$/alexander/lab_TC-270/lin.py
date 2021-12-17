
import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots()

x = np.arange(1, 10, 1.0/256)
y = 3*x + 2
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x, y, "r")
plt.show()
