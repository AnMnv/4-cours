from math import sqrt


h = 4.14*10**-15
c = 3*10**8
m = 9.1*10**-31
e = 1.6*10**-19

Una50 = 2.8
Una100 = 2.9

Vna50 = sqrt(2*Una50*e/m) 
Vna100 = sqrt(2*Una100*e/m) 
print(Vna50)
print(Vna100)

print("--------------------")

Uzn = 1.3
Uzn1 = 1.4
Vzn = sqrt(2*Uzn*e/m) 
Vzn1 = sqrt(2*Uzn1*e/m)
print(Vzn)
print(Vzn1)

print("--------------------")

Ucu50 = 3.3
Vcu = sqrt(2*Ucu50*e/m)
print(Vcu)


print("---------Ейнштейнова формула-----------")
a = h*1.5*10**15
b = (m*((13.2*10**5)**2))/2
print(a)
print(b)