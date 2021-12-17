from math import pi, sqrt

ro = 2.8
Rn = 2.1*10**-3
q =1.6*10**-19
n =  1/(q*Rn)
print("n = " , n, "m^-3")

eps = 11.7
eps0 = 8.8*10**-12
nplus = 2*10**25
lrez = 11.5*10**-6
c = 3*10**8
frez = c/lrez
m = (q**2 *nplus)/(eps*eps0*frez**2)
print("m = " , m, "kg")

hw = 0.088*10**-19
js = q*n*sqrt(hw/m)
print("js = ", '{0:10e}'.format(js), "A/m^2")
