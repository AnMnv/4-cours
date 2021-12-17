D1 = 2
D2 = 6
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
print(x)
R = [4, -14, 47, -194]
print(R)


y = [];
for n in range(5):
    RESULT = ""
    b = 0;
    for k in range(9):
        if (k) < 0 or (k) > len(x)-1 or (n-k) < 0 or (n-k) > len(R)-1:
            RESULT += ""
            b += 0;
        elif x[k]*R[n-k] < 0:
            RESULT += "+(" + str(x[k]*R[n-k]) + ")"
            b+= x[k]*R[n-k]
        else:
            RESULT += "+" + str(x[k]*R[n-k])
            b+= x[k]*R[n-k]
    y.append(b)
    if len(RESULT) == 0:
        print("0")
    else:
        print(RESULT[1:])
print(y)
