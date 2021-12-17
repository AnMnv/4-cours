from math import sqrt


h = 4.14*10**-15
c = 3*10**8
m = 9.1*10**-31
e = 1.6*10**-19

Una50 = 2.3
Una100 = 2.29

Vna50 = sqrt(2*Una50*e/m) 
Vna100 = sqrt(2*Una100*e/m) 
print(Vna50)
print(Vna100)

print("--------------------")

Uzn = 2.1
Uznn = 2.15
Vzn = sqrt(2*Uzn*e/m) 
Vznn = sqrt(2*Uznn*e/m) 
print(Vzn)
print(Vznn)

print("--------------------")

Ucu50 = 3.1
Ucu100 = 3.2
Vcu50 = sqrt(2*Ucu50*e/m)
Vcu100 = sqrt(2*Ucu100*e/m) 
print(Vcu50)
print(Vcu100)

print("---------Ейнштейнова формула-----------")
a = h*1.5*10**15
b = (m*((13.2*10**5)**2))/2
print(a)
print(b)