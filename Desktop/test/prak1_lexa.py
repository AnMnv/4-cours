#!/usr/bin/python
#-*- coding: utf8 -*-
import math
from math import sqrt
import os
s1=0.119;
s2=0.108;
s3=0.105;
u23_1=0.03;
u23_2=0.01;
u23_3=0.07;
i14_1=0.02;
i14_2=0.05;
i14_3=0.08;

os.system('cls||clear')

k=1.0/s1-1.0/(s2+s3)-1.0/(s1+s2)+1.0/s3;
ro1=((2.0*math.pi)/k)*(u23_1/i14_1)
ro2=((2.0*math.pi)/k)*(u23_2/i14_2)
ro3=((2.0*math.pi)/k)*(u23_3/i14_3)


print("    ro1,  		  ro2, 			 ro3")
print(ro1, ro2, ro3)
#значення точкової оцінки вимірюваної величини
m=(1.0/3.0)*(float(ro1)+float(ro2)+float(ro3))
print "\nm =", m
#значення оцінки середньоквадратичного відхилення одиничного вимірювання серед n вимірів
d=sqrt((1.0/3.0)*(((ro1-m)**2.0)+((ro2-m)**2.0)+((ro3-m)**2.0)))
print "середньокв. відхилення одиничного вимірювання серед n вимірів: ", d
#значення оцінки середньоквадратичного відхилення середнього арифметичного виконаних вимірів
d0=d/sqrt(3.0)
print "відхилення середнього арифметичного виконаних вимірів: ", d0
#вважаючи, що довірча ймовірність ρдй = 0,95, знаходимо квантиль
#Ts=0.05064
print('квантиль ts(0.975,2)')
#значення півширини довірчого інтервалу
ts = 4.3*0.975 
print ('ts',ts)
a=4.3*0.975*d0
#b=2.0*d0
print "Значення півширини довірчого інтервалу:", (a)
#значення абсцис кінців довірчого інтервалу
mn=m-a
#mn1=m-b

mv=m+a
#mv1=m+b

print "Мн: ",(mn)
print "Мв: ",(mv)
#відноснa похибку вимірювання
delta1=(a*100.0)/m
#delta2=(b*100.0)/m

print "Відносна похибкa вимірювання"
print "\ndelta =", (delta1) 
print "\n\n"
