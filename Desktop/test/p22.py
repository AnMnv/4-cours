#!/usr/bin/env python
# coding=utf8

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

h1 = D1+D2
h2 = M1+M2
h3 = -P1
h4 = P4

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

# сумма
MASS1 = [h1, h2, h3, h4]
MASS = [S1, S2, S3, S4, S5]

for n in range(9):
    RESULT = ""
    for m in range((N1+N2-1)+1):
        if (m) < 0 or (m) > 4 or (n-m) < 0 or (n-m) > 3:
            RESULT += ""
        elif MASS[m]*MASS1[n-m] < 0:
            RESULT += "+(" + str(MASS[m]*MASS1[n-m]) + ")"
        else:
            RESULT += "+" + str(MASS[m]*MASS1[n-m])
    print(RESULT[1:])

print("h =", "[", h1, h2, h3, h4, "]")
print("N1=", N1)
print("N2=", N2)
