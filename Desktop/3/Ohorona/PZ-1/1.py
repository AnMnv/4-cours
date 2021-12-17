
import matplotlib.pyplot as plt
from matplotlib.transforms import Affine2D
import numpy as np

R1 = 0.00030*1.7
R2 = 5*10**(-8) * 2024
R3 = 1.9*0.00072
R4 = 91*10**-6*1.9
R = R1+R2+R3+R4
print("R = ",'{0:10e}'.format(R))
vals = [R1*1000, R2*1000, R3*1000, R4*1000]
labels = ["R1", "R2", "R3", "R4"]
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, wedgeprops=dict(width=0.5))
fig.savefig('1.pdf')

R1 = 0.00160*1.45
R2 = 6*10**(-7) * 2024
R3 = 1.6*0.00084
R4 = 61*10**-6*1.6
RR = R1+R2+R3+R4
print("RR = ",'{0:10e}'.format(RR))
vals = [R1*1000, R2*1000, R3*1000, R4*1000]
labels = ["R1", "R2", "R3", "R4"]
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, wedgeprops=dict(width=0.5))
fig.savefig('2.pdf')
plt.show()
