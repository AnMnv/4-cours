
#!/usr/bin/python
#-*- coding: utf8 -*-
import os
T = 273.15
qqmax = 0.4
f = 10**12

#const
h = 4.135*10**(-15)
k = 8.617*10**(-5)

Ek = k*T
os.system("cls||clear")
print "Ek=", Ek, "eB"

Nq = (k*T)/(h*f)
print "Nq=", Nq

E = (h*f)/(Nq+1)
print "deltaE=", E


if E < Ek:
    print ("The quasi-elastic scattering condition is satisfied")
else:
	print ("The quasi-elastic scattering condition is NOT satisfied")