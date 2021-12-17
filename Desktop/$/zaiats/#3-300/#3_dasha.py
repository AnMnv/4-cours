
# AsGa
import numpy as np
import matplotlib.pyplot as plt
import math
import itertools

NA = 2.2*10**(16)   # cm^-4
ND = 3.8*10**(18)   # cm^-4
T = 300
k = 8.617333262*10**(-5)  # eB * K^-1
lp = 0.000986104   # cm
ln = 0.000075023  # cm
ft = 0.0258
E0 = 8.85*10**(-14)
E = 13.1
ni = 1.79*10**6.0
q = 1.6*10**(-19)
Nc = 4.7*10**17
Nv = 7.0*10**17

f0 = ft*math.log((NA*ND*ln*lp)/(ni**2.0))
f00 = q*(NA*lp**3+ND*ln**3)/(3*E*E0)
fft = f00/math.log((NA*ND*ln*lp)/(ni**2.0))

print("###")
print(f0)
print(f00)
print(fft)
# Ep
a1 = (q*NA) / (2*E*E0)
x1 = np.arange(-lp, 0, 0.000001)
Ep = a1 * (x1**2 - lp**2.0)
print(a1*lp**2)

# En
a2 = (q*ND) / (2*E*E0)
x2 = np.arange(0, ln, 0.00000001)
En = a2 * (x2**2 - ln**2.0)
print(a2*ln**2.0)

l_pr = ((3.0*E*E0*(f0-0.8*f0)/q)*(1/(NA)+2 /
        (math.sqrt(NA*ND))+1/(ND)))**(1.0/3.0)
print(l_pr)
lp1 = l_pr/(1+math.sqrt(NA/ND))
ln1 = l_pr - lp1
x11 = np.arange(-lp1, 0, 0.000001)
x21 = np.arange(0, ln1, 0.00000001)
Ep1 = a1 * (x11**2 - lp1**2.0)
En1 = a2 * (x21**2 - ln1**2.0)

l_pr2 = ((3.0*E*E0*(f0+2.0*f0)/q)*(1/(NA)+2 /
         (math.sqrt(NA*ND))+1/(ND)))**(1.0/3.0)
print(l_pr2)
lp2 = l_pr2/(1+math.sqrt(NA/ND))
ln2 = l_pr2 - lp2
x12 = np.arange(-lp2, 0, 0.000001)
x22 = np.arange(0, ln2, 0.00000001)
Ep2 = a1 * (x12**2 - lp2**2.0)
En2 = a2 * (x22**2 - ln2**2.0)
fig, ax = plt.subplots()
plt.plot(x1, Ep, 'g', label="рівноважний стан")
plt.plot(x2, En, 'g')
plt.plot(x11, Ep1, 'm', label="при прикладеній напрузі $0.8\cdot\phi_0$")
plt.plot(x21, En1, 'm')
plt.plot(x12, Ep2, 'b', label="при прикладеній напрузі $(-2)\cdot\phi_0$")
plt.plot(x22, En2, 'b')
plt.grid(True)
plt.xlabel("x, см")
#plt.title("Розподіл електрічного поля в плавному p-n переході")
plt.legend()
plt.savefig('/Users/antonmnacakanov/Desktop/III/TTE/#3/1.pdf', dpi=1000)
#plt.show()

print("------------------------------")
print("* В рівноважному стані")
print("ширина p області = ", x1[0])
print("ширина n області = ", x2[-1])

print("* 0.8")
print("ширина p області = ", x11[0])
print("ширина n області = ", x21[-1])

print("* -2")
print("ширина p області = ", x12[0])
print("ширина n області = ", x22[-1])
print("------------------------------")

#                  #################      fi       ########################

# fi_p
b1 = (q*NA) / (6.0*E*E0)
x3 = np.arange(-lp, 0.0, 0.000001)
fip = b1*(3*(lp**2)*x3 - x3**3 + 2*(lp**3))


# fi_n
b2 = (q*ND) / (6.0*E*E0)
x4 = np.arange(0.0, ln, 0.0000001)
fin = f00 + b2*(3*(ln**2)*x4 - x4**3 - 2*(ln**3))


fip1 = b1*(3*(lp1**2)*x11 - x11**3 + 2*(lp1**3))
fin1 = f0 - 0.8*f0 + b2*(3*(ln1**2)*x21 - x21**3 - 2*(ln1**3))

fip2 = b1*(3*(lp2**2)*x12 - x12**3 + 2*(lp2**3))
fin2 = f0 + 2.0*f0 + b2*(3*(ln2**2)*x22 - x22**3 - 2*(ln2**3))

plt.plot(x3, fip, 'm', label="рівноважний стан")
plt.plot(x4, fin, 'm')
plt.plot(x11, fip1, 'r', label="при прикладеній напрузі $0.8\cdot\phi_0$")
plt.plot(x21, fin1, 'r')
plt.plot(x12, fip2, 'g', label="при прикладеній напрузі $(-2)\cdot\phi_0$")
plt.plot(x22, fin2, 'g')
plt.grid(True)
plt.xlabel("x, см")
plt.ylabel("E, еВ")
#plt.title("Розподіл потенціалу в плавному p-n переході")
plt.legend()
plt.savefig('/Users/antonmnacakanov/Desktop/III/TTE/#3/2.pdf', dpi=1000)
plt.close(fig)
#plt.show()
print("------------------------------")
print("* В рівноважному стані")
print("ширина p області = ", x3[0])
print("ширина n області = ", x4[-1])

print("* 0.8")
print("ширина p області = ", x11[0])
print("ширина n області = ", x21[-1])

print("* -2")
print("ширина p області = ", x12[0])
print("ширина n області = ", x22[-1])
print("------------------------------")

# #########    енергетичні діаграми ідеалізованого p-n переходy  ##############

fig, ax = plt.subplots()
ax.axvline(x=0, lw=1, color='m', label="металургічна межа")
ax.axvline(x=-0.00039210400000005, lw=2, color='y', label="межа p-n переходу")

plt.plot(x3, -fip+(1.42/2), 'b', label="$E_C$")
plt.plot(x4, -fin+(1.42/2), 'b')
#plt.plot(x11, -fip1+(1.42/2), 'b')
#plt.plot(x21, -fin1+(1.42/2), 'b')
#plt.plot(x12, -fip2+(1.42/2), 'b')
#plt.plot(x22, -fin2+(1.42/2), 'b')

plt.plot(x3, -fip, 'r--', label="$E_i$")
plt.plot(x4, -fin, 'r--')
#plt.plot(x11, -fip1, 'r--')
#plt.plot(x21, -fin1, 'r--')
#plt.plot(x12, -fip2, 'r--')
#plt.plot(x22, -fin2, 'r--')

print("+++")
print(-fip[0]+(1.42/2))
print(-fin[len(fin)-1]+(1.42/2))
print(fip[0]+(1.42/2))
print(fin[len(fin)-1]+(1.42/2))
print("===")
Ecp = -fip[0]+(1.42/2)
Ecn = -fin[len(fin)-1]+(1.42/2)

Evp = -fip[0]-(1.42/2)
Evn = -fin[len(fin)-1]-(1.42/2)
Efip = (Ecp + Evp)/2# + k*T*math.log(math.sqrt(Nv/Nc))
Efin = (Ecn + Evn)/2# + k*T*math.log(math.sqrt(Nv/Nc))

Efp = Efip - k*T*math.log(NA*lp/ni)
Efn = Efin + k*T*math.log(ND*ln/ni)
print(Efip)
print(Efin)
print(Efp)
print(Efn)

print("Ecp = ", Ecp)
print("Ecn = ", Ecn)
print("висота потенціального бар'єру в рівнов. стані = ")
print("Evp = ", Evp)

xEf = [-lp, ln]
yEf = [Efp, Efp]


plt.plot(x3, -fip-(1.42/2), 'k', label="$E_V$")
plt.plot(x4, -fin-(1.42/2), 'k')
#plt.plot(x11, -fip1-(1.42/2), 'k')
#plt.plot(x21, -fin1-(1.42/2), 'k')
#plt.plot(x12, -fip2-(1.42/2), 'k')
#plt.plot(x22, -fin2-(1.42/2), 'k')
plt.plot(xEf, yEf, 'g', label="$E_F$")
plt.grid(True)
plt.xlabel("x, см")
plt.ylabel("E, еВ")
#plt.title("Енергетична діаграма ідеалізованого p-n переходу")
plt.legend()
plt.savefig('/Users/antonmnacakanov/Desktop/III/TTE/#3/3.pdf', dpi=1000)

#plt.show()

for (v, w) in zip(x3, -fip):
    if w < Efp:
        print("delta = ", v)
        break
# -----------------------ДОДАТОК-------------------------------



plt.plot(x3, -fip+(1.42/2), 'b', label="при прикладеній напрузі $0.8\cdot\phi_0$")
plt.plot(x4, -fin+(1.42/2), 'b')
plt.plot(x11, -fip1+(1.42/2), 'b')
plt.plot(x21, -fin1+(1.42/2), 'b')
plt.plot(x12, -fip2+(1.42/2), 'b')
plt.plot(x22, -fin2+(1.42/2), 'b')
print("------------------------------")
print("*  0.8")
print("ширина p області = ", x3[0])
print("ширина n області = ", x4[-1])
print()
print("--------------------------------------висота потенціального бар'єру###")
f0008 = f00 + (0.8)*f00
print("при 0.8 = ", f0008, "eB")
print()

plt.plot(x3, -fip, 'r--', label="рівноважний стан")
plt.plot(x4, -fin, 'r--')
plt.plot(x11, -fip1, 'r--')
plt.plot(x21, -fin1, 'r--')
plt.plot(x12, -fip2, 'r--')
plt.plot(x22, -fin2, 'r--')
print("*В рівноважному стані")
print("ширина p області = ", x11[0])
print("ширина n області = ", x21[-1])
print()
print("------------------------------висота потенціального бар'єру###")
print("рівноважний стан = ", f00, "eB")
print()

plt.plot(x3, -fip-(1.42/2), 'k', label="при прикладеній напрузі $(-2)\cdot\phi_0$")
plt.plot(x4, -fin-(1.42/2), 'k')
plt.plot(x11, -fip1-(1.42/2), 'k')
plt.plot(x21, -fin1-(1.42/2), 'k')
plt.plot(x12, -fip2-(1.42/2), 'k')
plt.plot(x22, -fin2-(1.42/2), 'k')
print("* -2")
print("ширина p області = ", x12[0])
print("ширина n області = ", x22[-1])
print()
print("------------------------------висота потенціального бар'єру -2  ###")
f002 = f00 + (-2)*f00
print("при -2 = ", f002, "eB")
print("------------------------------")
print()
plt.grid(True)
plt.xlabel("x, см")
plt.ylabel("E, еВ")
# plt.title("Енергетичні діаграми ідеалізованого p-n переходу")
plt.legend()
plt.savefig('/Users/antonmnacakanov/Desktop/III/TTE/#3/3.1.pdf', dpi=1000)
plt.show()
