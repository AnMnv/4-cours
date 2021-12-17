# -*- coding: utf-8 -*-
import math
import matplotlib.pyplot as plt

x = [11, -8, -7, 3, 9]
N = len(x)
FS = 1000*(2+4+0+5)
f = range(0,FS+1, FS/4)
#1-----------------------------------
print("---------------1---------------------")
print("C[m] = 1/N SUM_{n=0}^{N-1}{x[n]*exp(-2*PI*m*n*j/N)}")

C = []
A = []
PHI = []
for i in range(N):
    curr_C_real = 0;
    curr_C_im = 0;
    curr_str = "C["+str(i)+"] = 1/"+str(N)+"*SUM_{n=0}^{"+str(N-1)+"}{x[n]*exp(-2*PI*"+str(i)+"*n*j/"+str(N)+")}="
    for j in range(N):
        curr_C_real += round(1.0/N*x[j]*math.cos(-2.0*math.pi*i*j/N), 2)
        curr_C_im += round(1.0/N*x[j]*math.sin(-2.0*math.pi*i*j/N),2)
        curr_str+= "1/"+str(N)+"*"+str(x[i])+"*(cos(-2*PI*"+str(i)+"*"+str(j)+"/"+str(N)+")+j*sin(-2*PI*"+str(i)+"*"+str(j)+"/"+str(N)+"))+"
    curr_A = round(math.sqrt(curr_C_real**2+curr_C_im**2),2)
    curr_PHI = round(math.atan(curr_C_im/curr_C_real),2)
    curr_str = curr_str[:-1]+" = "+str(curr_C_real) + " + j*"+str(curr_C_im) + " = " + str(curr_A) + "*e^{"+str(curr_PHI)+"}\n"
    curr_str +="A["+str(i)+"]=SQRT{REAL(C["+str(i)+"])^2+IM(C["+str(i)+")^2} = SQRT{"+str(curr_C_real**2)+"+"+str(curr_C_im**2)+"} = "+str(curr_A)+"\n"
    curr_str +="PHI["+str(i)+"]=arctg{IM(C["+str(i)+"])/REAL(C["+str(i)+")} = arctg{"+str(curr_C_im)+"/"+str(curr_C_real)+"} = "+str(curr_PHI)+"\n"
    print(curr_str)
    C.append([curr_C_real, curr_C_im])
    A.append(curr_A)
    PHI.append(curr_PHI)




#2--------------------------------
X = []

def comp_sum(a, b):
    return [a[0]+b[0], a[1]+b[1]]

def comp_mul(a, b):
    return [a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]]

for i in range(N):
    curr_X = [0, 0];
    curr_str = "X["+str(i)+"] = SUM_{n=0}^{"+str(N-1)+"}{C[n]*exp(-2*PI*"+str(i)+"*n*j/"+str(N)+")}="
    curr_str1 = ""
    for j in range(N):
        curr_str+= "("+str(C[j][0])+"+j*"+str(C[j][1])+")*(cos(-2*PI*"+str(i)+"*"+str(j)+"/"+str(N)+")+j*sin(-2*PI*"+str(i)+"*"+str(j)+"/"+str(N)+"))+"
        curr_str1+="("+str(C[j][0])+"+j*"+str(C[j][1])+")*("+str(round(math.cos(2*math.pi*i*j/N),2))+"+j*"+str(round(math.sin(2*math.pi*i*j/N),2))+")+"
        curr_X = comp_sum(curr_X, comp_mul(C[j], [round(math.cos(2*math.pi*i*j/N),2), round(math.sin(2*math.pi*i*j/N),2)]))
    print(curr_str[:-1]+" = " +curr_str1[:-1] + " = "+ str(curr_X[0]) + "+j*"+ str(curr_X[1]) )
    X.append(curr_X[0])

SIGMA = 0
SIGMA_str = "SIGMA = SQRT{1/N*SUM_{n=0}^{N-1}{{x[n]-X[n]}^2} = SQRT{1/"+str(N)+"*SUM_{n=0}^{"+str(N-1)+"}{{x[n]-X[n]}^2}} = SQRT{1/"+str(N)+"*("
SIGMA_str1 = ""
for i in range(N):
    SIGMA += (x[i]-X[i])**2
    SIGMA_str += "("+str(x[i]) + "-" + str(X[i])+")^2+"
    SIGMA_str1 += str(x[i]-X[i])+"^2+"

SIGMA = math.sqrt(1.0/N*SIGMA)
SIGMA_str = SIGMA_str[:-1]+")} = SQRT{1/"+str(N)+"*("+SIGMA_str1[:-1]+")} = "+str(SIGMA)

print(SIGMA_str)


plt.figure()

#plt.subplot(411)
#plt.stem(f, x)

plt.subplot(211)
plt.stem(f, A)

plt.subplot(212)
plt.stem(f, PHI)

#plt.subplot(414)
#plt.stem(f, X)
plt.show()


#3---------------------------------

xw = x + [0,0,0]
H8 = [[1, 1, 1, 1, 1, 1, 1, 1],
      [1,-1, 1,-1, 1,-1, 1,-1],
      [1, 1,-1,-1, 1, 1,-1,-1],
      [1,-1,-1, 1, 1,-1,-1, 1],
      [1, 1, 1, 1,-1,-1,-1,-1],
      [1,-1, 1,-1,-1, 1,-1, 1],
      [1, 1,-1,-1,-1,-1, 1, 1],
      [1,-1,-1, 1,-1, 1, 1,-1]]

def calc_W(H, x):
    res = []
    res_str = "";
    for i in range(8):
        curr_res = 0;
        for j in range(8):
            curr_res += H[i][j]*x[j]
            res_str += str(H[i][j]*x[j])+"+"
        res_str = res_str[:-1] + "\n"
        res.append(float(curr_res)/8)
    return [res, res_str]

[W, W_str] = calc_W(H8, xw)
print("---------------3---------------------")
print(W_str)
print(W)

#4--------------------------------
[XW, XW_str] = calc_W(H8, W)
print("---------------4---------------------")
print(XW_str)
print(XW)

plt.figure()

#plt.subplot(311)
#plt.stem(range(8), xw)

#plt.subplot(312)
plt.stem(range(8), W)

#plt.subplot(313)
#plt.stem(range(8), XW)

plt.show()

#5------------------------------------------
print("---------------5---------------------")
print("знаменник")
Z = 0;
Z_str = "Z = 1/N*SQRT{SUM_{n=0}^{N-1}{x_1[n]}*SUM_{n=0}^{N-1}{x_2[n]}} = 1/"+str(N)+"*SQRT{SUM_{n=0}^{"+str(N-1)+"}{x_1[n]}*SUM_{n=0}^{"+str(N-1)+"}{x_2[n]}} = 1/"+str(N)+"SQRT{("
Z_str1 = ""
for i in range(len(x)):
    Z+=x[i]**2
    Z_str+= str(x[i])+"^2+"
    Z_str1+= str(x[i]**2)+"+"
Z = 1.0/N*Z
Z_str = Z_str[:-1] + ")^2} = 1/"+str(N)+"*(" + Z_str1[:-1] + ") = "+str(Z)
print(Z_str)

r12 = []
for i in range(len(x)):
    curr_r12 = 0;
    curr_r12_str = "r12["+str(i)+"] = 1/N*SUM_{n=0}^{N-1}{x[n]*x[n-1]} = 1/"+str(N)+"*("
    curr_r12_str1 = "1/"+str(N)+"*("
    curr_r12_str2 = "1/"+str(N)+"*("
    for j in range(len(x)):
        curr_r12 += x[j]*(x[j-i] if (j-i)>=0 else 0);
        curr_r12_str += "x["+str(j)+"]*x["+str(j-i)+"]+"
        curr_r12_str1+= str(x[j]) + "*" + str(x[j-i] if (j-i)>=0 else 0) + "+"
        curr_r12_str2+= str(x[j]*(x[j-i] if (j-i)>=0 else 0)) + "+"
    curr_r12 = 1.0/N*curr_r12;
    r12.append(curr_r12)
    curr_r12_str = curr_r12_str[:-1] + ") = " + curr_r12_str1[:-1] + ") = " + curr_r12_str1[:-1] + ") = " + str(curr_r12)
    print(curr_r12_str)

B12 = []
for i in range(len(x)):
    B12.append(r12[i]/Z)
    print("B12["+str(i)+"] = r12["+str(i)+"]/Z = " + str(r12[i]) + "/" + str(Z) + " = "+str(B12[i]))


plt.figure()
plt.stem(range(-4, 5), B12[::-1][:-1]+B12)
plt.show()
