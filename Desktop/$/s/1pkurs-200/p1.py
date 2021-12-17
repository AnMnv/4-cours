D1 = 2
D2 = 4
M1 = 0
M2 = 5
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
# сигнал
print("x[n]=", "[", S1, S2, S3, S4, S5, "]")
print("N1=", N1)
print("N2=", N2)
# сумма
MASS = [S1, S2, S3, S4, S5]
for n in range(9):
    RESULT = ""
    for i in range(-N1, N2+1):
        if (n-i) < 0 or (n-i) > 4:
            RESULT += ""
        else:
            RESULT += "+(" + str(MASS[n-i]) + ")"
    RESULT = RESULT[1:]
    print(RESULT)
