import math

s = 661.5
n = 7.0
npar = 6.0

a = (s * 12.0)
b = (n ** 2.0 *(npar ** 3.0 - npar))
W = (a/b)
print(W) 



a = 0.91
b = 0.09
cpov =  14343
q = 5000
x = 7000

cp = a*cpov*q + b*cpov*x 
print(cp)


cdog = 21300

q1 = (b*cpov*x)/(cdog-a-cpov)
print(q1)

q2 = (b*cpov*x*1.2)/(cdog-a-cpov*1.2)
print(q2)

p = (cdog-cpov)*q2
print(p)

qwe = b*cpov*x 
print(qwe)