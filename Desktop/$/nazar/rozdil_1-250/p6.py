#!/usr/bin/env python
# coding=utf8
D1 = 1
D2 = 0
M1 = 0
M2 = 3
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
x = [S1, S2, S3, S4, S5]
R = []
for n in range(3):
    R.append(H1[n] + H2[n])
print("h", R)

h_e = []
n = 0
while True:
    a = ""
    b = 0
    for k in range(6):
        if (k) < 0 or (k) > len(H1)-1 or (n-k) < 0 or (n-k) > len(H2)-1:
            a += ""
            b += 0
        elif H1[k]*H2[n-k] < 0:
            a += "+(" + str(H1[k]*H2[n-k]) + ")"
            b += H1[k]*H2[n-k]
        else:
            a += "+" + str(H1[k]*H2[n-k])
            b += H1[k]*H2[n-k]
    if len(a) == 0:
        print("0")
    else:
        print("h_екв =", a[1:])
    n += 1
    if b != 0:
        h_e.append(b)
    else:
        break
print(h_e)


y = []
for n in range(9):
    RESULT = ""
    b = 0;
    for k in range(9):
        if (k) < 0 or (k) > len(h_e)-1 or (n-k) < 0 or (n-k) > len(x)-1:
            RESULT += ""
            b += 0
        elif h_e[k]*x[n-k] < 0:
            RESULT += "+(" + str(h_e[k]*x[n-k]) + ")"
            b += h_e[k]*x[n-k]
        else:
            RESULT += "+" + str(h_e[k]*x[n-k])
            b += h_e[k]*x[n-k]
    if len(RESULT) == 0:
        print("0")
    else:
        print("y [] =", RESULT[1:])
    y.append(b)
print("y[n]+", M1+M2, "*y[n-1]", -P1, "*y[n-2]", "+", D1+D2, "*y[n-3]=", M2+1,
      "*x[n]", -(M1+2), "*x[n-1]", -M2, "*x[n-2]+", (M1+D2+1), "*x[n-3]+",
      P4+4, "*x[n-4]")
print(y)

koef = [3, -2, 1, 4, -2, -3, 1, 5]
x = [1, 0, 0, 0, 0]
y = [0, 0, 0, 0]

for i in range(4):
    res = "y["+str(i)+"] = "
    y[i] =   3*(y[i-1] if (i-1)>=0 else 0)
    res += "3*"+str((y[i-1] if (i-1)>=0 else 0))
    y[i] += -2*(y[i-2] if (i-2)>=0 else 0)
    res += "-2*"+str((y[i-2] if (i-2)>=0 else 0))
    y[i] +=  1*(y[i-3] if (i-3)>=0 else 0)
    res += "+1*"+str((y[i-3] if (i-3)>=0 else 0))
    y[i] +=  4*(x[i] if (i)>=0 else 0)
    res += "+4*"+str((x[i] if (i)>=0 else 0))
    y[i] += -2*(x[i-1] if (i-1)>=0 else 0)
    res += "-2*"+str((x[i-1] if (i-1)>=0 else 0))
    y[i] += -3*(x[i-2] if (i-2)>=0 else 0)
    res += "-3*"+str((x[i-2] if (i-2)>=0 else 0))
    y[i] +=  1*(x[i-3] if (i-3)>=0 else 0)
    res += "+1*"+str((x[i-3] if (i-3)>=0 else 0))
    y[i] +=  5*(x[i-4] if (i-4)>=0 else 0)
    res += "+5*"+str((x[i-4] if (i-4)>=0 else 0))
    res += " = " + str(y[i])
    print(res)
print("y = "+str(y))
