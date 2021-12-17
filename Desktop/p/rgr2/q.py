from math import tan
import matplotlib.pyplot as plt
import numpy as np

Z0=46
x1 = np.arange(0,0.05,0.00001)
for i in range(len(x1)):
    if x1[i]==0.028:
        print(i)
print(tan(1.652))
ReZ=[Z0*(46*25+25*25*tan(59*x)+25*25*tan(59*x)+46*25*tan(59*x)*tan(59*x))/((46+25*tan(59*x))*(46+25*tan(59*x))+625*tan(59*x)*tan(59*x)) for x in x1]
ImZ=[Z0*(-25*25*tan(59*x)-25*46-25*25*tan(59*x)+46*46*tan(59*x)+46*25*tan(59*x)*tan(59*x))/((46+25*tan(59*x))*(46+25*tan(59*x))+625*tan(59*x)*tan(59*x)) for x in x1]
print(ImZ[2800])

plt.scatter(0.028,46)
plt.plot(x1,ImZ,label='Im(Z(x))')
plt.plot(x1,ReZ,label='Re(Z(x))')
plt.legend()
plt.tick_params(axis='both', labelsize=14)
plt.xlabel('X, [м] ',size=14)
plt.ylabel('Z, [Ом] ',size=14)
plt.grid(True)
plt.show()

plt.figure()
x1 = np.arange(0,0.03,0.00001)
V = [(1.189+0.87*cos(2*59*x-1.198))(1/2) for x in x1]
I = [(1.189-0.87*cos(2*59*x-1.198))(1/2) for x in x1]
plt.plot(x1,V,label='Розподіл амплітуд наруги')
plt.plot(x1,I,label='Розподіл амплітуд струму')
plt.tick_params(axis='both', labelsize=14)
plt.xlabel('X, [м] ',size=14)
plt.ylabel('V(x)/Vmax;I(x)/Imax',size=14)
plt.legend()
plt.grid(True)
plt.show()
