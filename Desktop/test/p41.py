#!/usr/bin/env python
#coding=utf8
D1 = 1
D2 = 4
M1 = 1
M2 = 2
P1 = 2
P2 = 0
P3 = 0
P4 = 1

S1 = D1+D2+5     # 0
S2 = -(M1+M2+3)  # 1
S3 = -(M2+2)     # 2
S4 = P4+D1+M1    # 3
S5 = M1+M2+D2    # 4

N1 = M1+D2+1
if N1 <= 3:
    N1 = N1
else:
    N1 = 3

N2 = D1+D2+M2+1
if N2 <= 4:
    N2 = N2
else:
    N2 = 4

h11 = P4
h12 = M2+D2+1
h13 = M1

h21 = P1
h22 = D1
h23 = D1+D2

H1 = [h11, h12, h13]
H2 = [h21, h22, h23]

print("h1 =", H1)
print("h2 =", H2)
print("x[n]=", "[", S1, S2, S3, S4, S5, "]")
x = [13, -6, -5, 3, 9]
R = []
for n in range(3):
    R.append(H1[n] + H2[n])
print("h", R)

for n in range(6):
    a = ""
    for k in range(3):
        if (k) < 0 or (k) > 4 or (n-k) < 0 or (n-k) > 2:
            a += ""
        elif H1[k]*H2[n-k] < 0:
            a += "+(" + str(H1[k]*H2[n-k]) + ")"
        else:
            a += "+" + str(H1[k]*H2[n-k])
    if len(a) == 0:
        print("0")
    else:
        print("h_екв =", a[1:])
h_e = [2, 22, 28, 80]

for n in range(9):
    RESULT = ""
    for k in range(4):
        if (k) < 0 or (k) > 3 or (n-k) < 0 or (n-k) > 4:
            RESULT += ""
        elif h_e[k]*x[n-k] < 0:
            RESULT += "+(" + str(h_e[k]*x[n-k]) + ")"
        else:
            RESULT += "+" + str(h_e[k]*x[n-k])
    if len(RESULT) == 0:
        print("0")
    else:
        print("y [] =", RESULT[1:])
print("y[n]+", M1+M2, "*y[n-1]", -P1, "*y[n-2]", "+", D1+D2, "*y[n-3]=", M2+1,
      "*x[n]", -(M1+2), "*x[n-1]", -M2, "*x[n-2]+", (M1+D2+1), "*x[n-3]+",
      P4+4, "*x[n-4]")
