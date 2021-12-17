import numpy as np
import matplotlib.pyplot as plt
import math
import scipy as sc
from scipy import signal

#p1
T=1
F=[2,2.5,40,100,600]
fs=128
t=np.arange(0,T-1/fs,1/fs)
f=np.arange(0,fs-1/T,1/T)
j=1
y=[]
plt.figure(figsize=[22,5])
for i in range(len(F)):
    y.append([math.sin(2*math.pi*F[i]*t[k]) for k in range(len(t))])
    y=np.asarray(y)
    y=y.transpose()
    s=2*abs(np.fft.fft2(y))/len(t)
    plt.subplot(len(F),2,j)
    plt.plot(t,y)
    plt.grid()
    plt.xlabel('Час,с')
    plt.ylabel('Напруга,В')
    plt.subplot(len(F),2,j+1)
    plt.stem(f,s)
    plt.xlim([0,fs/2])
    plt.xlabel('Частота,Гц')
    plt.ylabel('Величина')
    j=j+2
    y1=y
    y=[]
plt.show()
#p2+-
# fs=256
# T=10
# T1=20
# F=[10,100]
# t=np.arange(0,T-1/fs,1/fs)
# f=np.arange(0,fs-1/T,1/T)
# t1=np.arange(0,T1-1/fs,1/fs)
# t1=np.delete(t1,-1)
# f1=np.arange(0,fs-1/T1,1/T1)
# f1=np.delete(f1,-1)
# y=[]

# y.append([math.sin(2*math.pi*F[0]*t[k]) for k in range(len(t))])
# y=np.asarray(y)
# y=y.transpose()

# y1=[]
# y1.append([math.sin(2*math.pi*F[1]*t[k]) for k in range(len(t))])
# y1=np.asarray(y1)
# y1=y1.transpose()
    
# ysum=y+y1
# plt.figure(figsize=[22,5])
# ssum=2*abs(np.fft.fft2(ysum))/len(t)
# plt.subplot(3,2,1)
# plt.plot(t,ysum)
# plt.grid()
# plt.xlabel('Час,с')
# plt.ylabel('Напруга,В')
# plt.subplot(3,2,2)
# plt.stem(f,ssum)
# plt.xlim([0,fs/2])
# plt.xlabel('Частота,Гц')
# plt.ylabel('Величина')

# yp2=y*2
# y1p2=y1*2
# yyp2=np.vstack((yp2, y1p2))
# sp2=2*abs(np.fft.fft2(yyp2))/len(t1)

# plt.subplot(3,2,3)
# plt.plot(t1,yyp2)
# plt.grid()
# plt.xlabel('Час,с')
# plt.ylabel('Напруга,В')
# plt.subplot(3,2,4)
# plt.stem(f1,sp2)
# plt.xlim([0,fs/2])
# plt.xlabel('Частота,Гц')
# plt.ylabel('Величина')

# yp2=y*2
# y1p2=y1*2
# yyp3=np.vstack((y1p2,yp2))
# sp3=2*abs(np.fft.fft2(yyp3))/len(t1)

# plt.subplot(3,2,5)
# plt.plot(t1,yyp3)
# plt.grid()
# plt.xlabel('Час,с')
# plt.ylabel('Напруга,В')
# plt.subplot(3,2,6)
# plt.stem(f1,sp3)
# plt.xlim([0,fs/2])
# plt.xlabel('Частота,Гц')
# plt.ylabel('Величина')



#p3+
# fs=128
# T=3
# t=np.arange(0,T-1/fs,1/fs)
# f=np.arange(0,fs-1/T,1/T)

# plt.figure(figsize=[22,5])

# s1=np.sin(2*np.pi*20*t);

# start=int((1.05*len(t))/T)
# end=start+10
# s1[start:end]=0

# s=2*abs(np.fft.fft(s1))/len(t)
# s=np.append(s,s[-1])
# plt.subplot(2,2,1)
# plt.plot(t,s1)
# plt.grid()
# plt.xlabel('Час,с')
# plt.ylabel('Напруга,В')
# plt.subplot(2,2,2)
# plt.stem(f,s)
# plt.xlim([0,fs/2])
# plt.xlabel('Частота,Гц')
# plt.ylabel('Величина')

# s1=np.sin(2*np.pi*20*t);
# start=int((2*len(t))/T)
# end=start+10
# s1[start:end]=0

# s=2*abs(np.fft.fft(s1))/len(t)
# s=np.append(s,s[-1])
# plt.subplot(2,2,3)
# plt.plot(t,s1)
# plt.grid()
# plt.xlabel('Час,с')
# plt.ylabel('Напруга,В')
# plt.subplot(2,2,4)
# plt.stem(f,s)
# plt.xlim([0,fs/2])
# plt.xlabel('Частота,Гц')
# plt.ylabel('Величина')


#p4+
# fs=512
# T=3
# t=np.arange(0,T-1/fs,1/fs)
# f=np.arange(0,fs-1/T,1/T)
# f=np.delete(f,-1)
# F=[10,100]
# j=1
# y=[]
# plt.figure(figsize=[22,5])
# for i in range(len(F)):
#     y.append([signal.square(2*np.pi*F[i]*t[k]) for k in range(len(t))])
#     y=np.asarray(y)
#     y=y.transpose()
#     s=2*abs(np.fft.fft2(y))/len(t)
#     plt.subplot(len(F),2,j)
#     plt.plot(t,y);
#     plt.xlabel('Час,с')
#     plt.ylabel('Напруга,В')
#     plt.subplot(len(F),2,j+1)
#     plt.stem(f,s)
#     plt.xlim([0,fs/2])
#     plt.xlabel('Частота,Гц')
#     plt.ylabel('Величина')
#     j=j+2
#     y=[]

#p5+
# fs=512
# T=30
# t=np.arange(0,T-1/fs,1/fs)
# f=np.arange(0,fs-1/T,1/T)
# F=[0.1,1,10]
# j=1
# plt.figure(figsize=[22,5])
# for i in range(len(F)):
    
#     s=np.zeros((len(t),))
#     end=int((F[i]*len(t))/T)
#     s[0:end] = 1
#     ss=2*np.fft.fft(s)/len(t)
    
#     ssa=abs(ss)
#     ssf=np.angle(ss)
    
#     plt.subplot(len(F),3,j)
#     plt.plot(t,s)
#     plt.xlabel('Час,с')
#     plt.ylabel('Напруга,В')
#     plt.subplot(len(F),3,j+1)
#     plt.stem(f,ssa)
#     plt.xlim([0,fs/2]);
#     plt.xlabel('Частота,Гц')
#     plt.ylabel('Величина')
#     plt.subplot(len(F),3,j+2)
#     plt.stem(f,ssf)
#     plt.xlim([0,fs/1])
#     plt.xlabel('Частота,Гц')
#     plt.ylabel('Значення')
#     j=j+3

# j=1
# plt.figure(figsize=[22,5])
# for i in range(len(F)):
    
#     s=np.zeros((len(t),))
#     start=int((5*len(t))/T)
#     end=int((F[i]*len(t))/T)
#     s[start:end+start] = 1
#     ss=2*np.fft.fft(s)/len(t)
    
#     ssa=abs(ss)
#     ssf=np.angle(ss)
    
#     plt.subplot(len(F),3,j)
#     plt.plot(t,s)
#     plt.xlabel('Час,с')
#     plt.ylabel('Напруга,В')
#     plt.subplot(len(F),3,j+1)
#     plt.stem(f,ssa)
#     plt.xlim([0,fs/2]);
#     plt.xlabel('Частота,Гц')
#     plt.ylabel('Величина')
#     plt.subplot(len(F),3,j+2)
#     plt.stem(f,ssf)
#     plt.xlim([0,fs/1])
#     plt.xlabel('Частота,Гц')
#     plt.ylabel('Значення')
#     j=j+3

#p6+
# fs=256
# T=10
# t=np.arange(0,T-1/fs,1/fs)
# f=np.arange(0,fs-1/T,1/T)
# plt.figure(figsize=[22,5])
# s=np.random.sample((1, len(t)))
# s=s.transpose()
# ss=2*np.fft.fft(s)/len(t)
# ssa=abs(ss);
# plt.subplot(2,1,1)
# plt.plot(t,s)
# plt.xlabel('Час,с')
# plt.ylabel('Напруга,В')
# plt.subplot(2,1,2)
# plt.stem(f,ssa)
# plt.xlim([0,fs/2])
# plt.xlabel('Частота,Гц')
# plt.ylabel('Значення')

#p7
# T=0.5
# F=20
# fs=128
# t=np.arange(0,T-1/fs,1/fs)
# t1=t
# f=np.arange(0,fs-1/T,1/T)
# f1=f
# y=[]
# y.append([math.sin(2*math.pi*F*t[k]) for k in range(len(t))])
# y=np.asarray(y)
# y=y.transpose()
# k=0
# while k<(T*fs):
#     y=np.append(y,np.random.normal(10))
#     t=np.append(t,t[-1]+1/fs)
#     f=np.append(f,f[-1]+1/T)
#     k=k+1
    
# s=2*abs(np.fft.fft(y))/len(t)
# plt.figure(figsize=[22,5])
# plt.subplot(5,2,1)
# plt.plot(t,y)
# plt.grid()
# plt.xlabel('Час,с')
# plt.ylabel('Напруга,В')
# plt.subplot(5,2,2)
# plt.stem(f,s)
# plt.xlabel('Частота,Гц')
# plt.ylabel('Величина')

# k=0
# while k<(1*fs):
#     y=np.append(y,np.random.normal(10))
#     t=np.append(t,t[-1]+1/fs)
#     f=np.append(f,f[-1]+1/T)
#     k=k+1
    
# s=2*abs(np.fft.fft(y))/len(t)
# plt.subplot(5,2,3)
# plt.plot(t,y)
# plt.grid()
# plt.xlabel('Час,с')
# plt.ylabel('Напруга,В')
# plt.subplot(5,2,4)
# plt.stem(f,s)
# plt.xlabel('Частота,Гц')
# plt.ylabel('Величина')

# k=0
# while k<(10*fs):
#     y=np.append(y,np.random.normal(10))
#     t=np.append(t,t[-1]+1/fs)
#     f=np.append(f,f[-1]+1/T)
#     k=k+1
    
# s=2*abs(np.fft.fft(y))/len(t)
# plt.subplot(5,2,5)
# plt.plot(t,y)
# plt.grid()
# plt.xlabel('Час,с')
# plt.ylabel('Напруга,В')
# plt.subplot(5,2,6)
# plt.stem(f,s)
# plt.xlabel('Частота,Гц')
# plt.ylabel('Величина')

# k=0
# while k<(100*fs):
#     y=np.append(y,np.random.normal(10))
#     t=np.append(t,t[-1]+1/fs)
#     f=np.append(f,f[-1]+1/T)
#     k=k+1
    
# s=2*abs(np.fft.fft(y))/len(t)
# plt.subplot(5,2,7)
# plt.plot(t,y)
# plt.grid()
# plt.xlabel('Час,с')
# plt.ylabel('Напруга,В')
# plt.subplot(5,2,8)
# plt.stem(f,s)
# plt.xlabel('Частота,Гц')
# plt.ylabel('Величина')

# k=0
# while k<(1000*fs):
#     y=np.append(y,np.random.normal(10))
#     t=np.append(t,t[-1]+1/fs)
#     f=np.append(f,f[-1]+1/T)
#     k=k+1
    
# s=2*abs(np.fft.fft(y))/len(t)
# plt.subplot(5,2,9)
# plt.plot(t,y)
# plt.grid()
# plt.xlabel('Час,с')
# plt.ylabel('Напруга,В')
# plt.subplot(5,2,10)
# plt.stem(f,s)
# plt.xlabel('Частота,Гц')
# plt.ylabel('Величина')




# T=0.5
# F=20
# fs=128
# t=np.arange(0,T-1/fs,1/fs)
# f=np.arange(0,fs-1/T,1/T)
# y=[]
# y.append([math.sin(2*math.pi*F*t[k]) for k in range(len(t))])
# y=np.asarray(y)
# y=y.transpose()
# k=0
# while k<(T*fs):
#     y=np.append(y,np.random.normal(10))
#     t=np.append(t,t[-1]+1/fs)
#     f=np.append(f,f[-1]+1/T)
#     k=k+1
    
# s=2*abs(np.fft.fft(y))/len(t)
# plt.figure(figsize=[22,5])
# plt.subplot(4,2,1)
# plt.plot(t,y)
# plt.grid()
# plt.xlabel('Час,с')
# plt.ylabel('Напруга,В')
# plt.subplot(4,2,2)
# plt.stem(f,s)
# plt.xlabel('Частота,Гц')
# plt.ylabel('Величина')
# plt.xlim([0,100])

# T=0.5
# F=20
# fs=1280
# t=np.arange(0,T-1/fs,1/fs)
# f=np.arange(0,fs-1/T,1/T)
# y=[]
# y.append([math.sin(2*math.pi*F*t[k]) for k in range(len(t))])
# y=np.asarray(y)
# y=y.transpose()
# k=0
# while k<(T*fs):
#     y=np.append(y,np.random.normal(10))
#     t=np.append(t,t[-1]+1/fs)
#     f=np.append(f,f[-1]+1/T)
#     k=k+1
    
# s=2*abs(np.fft.fft(y))/len(t)
# plt.subplot(4,2,3)
# plt.plot(t,y)
# plt.grid()
# plt.xlabel('Час,с')
# plt.ylabel('Напруга,В')
# plt.subplot(4,2,4)
# plt.stem(f,s)
# plt.xlabel('Частота,Гц')
# plt.ylabel('Величина')
# plt.xlim([0,100])

# T=0.5
# F=20
# fs=12800
# t=np.arange(0,T-1/fs,1/fs)
# f=np.arange(0,fs-1/T,1/T)
# y=[]
# y.append([math.sin(2*math.pi*F*t[k]) for k in range(len(t))])
# y=np.asarray(y)
# y=y.transpose()
# k=0
# while k<(T*fs):
#     y=np.append(y,np.random.normal(10))
#     t=np.append(t,t[-1]+1/fs)
#     f=np.append(f,f[-1]+1/T)
#     k=k+1
    
# s=2*abs(np.fft.fft(y))/len(t)
# plt.subplot(4,2,5)
# plt.plot(t,y)
# plt.grid()
# plt.xlabel('Час,с')
# plt.ylabel('Напруга,В')
# plt.subplot(4,2,6)
# plt.stem(f,s)
# plt.xlabel('Частота,Гц')
# plt.ylabel('Величина')
# plt.xlim([0,100])

# T=0.5
# F=20
# fs=128000
# t=np.arange(0,T-1/fs,1/fs)
# f=np.arange(0,fs-1/T,1/T)
# y=[]
# y.append([math.sin(2*math.pi*F*t[k]) for k in range(len(t))])
# y=np.asarray(y)
# y=y.transpose()
# k=0
# while k<(T*fs):
#     y=np.append(y,np.random.normal(10))
#     t=np.append(t,t[-1]+1/fs)
#     f=np.append(f,f[-1]+1/T)
#     k=k+1
    
# s=2*abs(np.fft.fft(y))/len(t)
# plt.subplot(4,2,7)
# plt.plot(t,y)
# plt.grid()
# plt.xlabel('Час,с')
# plt.ylabel('Напруга,В')
# plt.subplot(4,2,8)
# plt.stem(f,s)
# plt.xlabel('Частота,Гц')
# plt.ylabel('Величина')
# plt.xlim([0,100])

#p8+
# T=1
# F=20.5
# fs=1000
# t=np.arange(0,T-1/fs,1/fs)
# f=np.arange(0,fs-1/T,1/T)
# y=[]
# y.append([math.sin(2*math.pi*F*t[k]) for k in range(len(t))])
# y=np.asarray(y)
# y=y.transpose()
# y1=y
# f1=f

# s=2*abs(np.fft.fft2(y))/len(t)
# plt.figure(figsize=[22,8])
# plt.subplot(3,2,1)
# plt.plot(t,y)
# plt.grid()
# plt.xlabel('Час,с')
# plt.ylabel('Напруга,В')
# plt.subplot(3,2,2)
# plt.stem(f,s)
# plt.xlim([0,fs/2])
# plt.xlabel('Частота,Гц')
# plt.ylabel('Величина')

# i = 0
# while i < 10:
#     a=f[-1]+0.01
#     y=np.append(y,0)
#     f=np.append(f,a)
#     i = i + 1
# s=2*abs(np.fft.fft(y))/len(t)
# plt.subplot(3,2,3)
# plt.stem(f,s,label='+10')
# plt.xlim([19,22])
# plt.xlabel('Частота,Гц')
# plt.ylabel('Величина')
# plt.legend()

# y=y1
# f=f1
# i = 0
# while i < 100:
#     a=f[-1]+0.01
#     y=np.append(y,0)
#     f=np.append(f,a)
#     i = i + 1
# s=2*abs(np.fft.fft(y))/len(t)
# plt.subplot(3,2,4)
# plt.stem(f,s,label='+100')
# plt.xlim([19,22])
# plt.xlabel('Частота,Гц')
# plt.ylabel('Величина')
# plt.legend()

# y=y1
# f=f1
# i = 0
# while i < 1000:
#     a=f[-1]+0.01
#     y=np.append(y,0)
#     f=np.append(f,a)
#     i = i + 1
# s=2*abs(np.fft.fft(y))/len(t)
# plt.subplot(3,2,5)
# plt.stem(f,s,label='+1000')
# plt.xlim([19,22])
# plt.xlabel('Частота,Гц')
# plt.ylabel('Величина')
# plt.legend()

# y=y1
# f=f1
# i = 0
# while i < 10000:
#     a=f[-1]+0.01
#     y=np.append(y,0)
#     f=np.append(f,a)
#     i = i + 1
# s=2*abs(np.fft.fft(y))/len(t)
# plt.subplot(3,2,6)
# plt.stem(f,s,label='+10000')
# plt.xlim([19,22])
# plt.xlabel('Частота,Гц')
# plt.ylabel('Величина')
# plt.legend()

#p9+
# fs=256
# T=1
# t=np.arange(0,T-1/fs,1/fs)
# f=np.arange(0,fs-1/T,1/T)
# s=np.sin(2*math.pi*t*100)
# ss=np.fft.fft(s)
# iss=np.fft.ifft(ss)
# plt.figure(figsize=[22,5])
# plt.subplot(2,1,1)
# plt.plot(t,s)
# plt.title('Вхідний сигнал')
# plt.xlabel('Час,с')
# plt.ylabel('Напруга,В')
# plt.subplot(2,1,2)
# plt.plot(t,iss)
# plt.title('Перетворений сигнал')
# plt.xlabel('Час,с')
# plt.ylabel('Напруга,В')
# a=np.std((s,iss))


#p10+
# def sg(filename,fs,F,T):
#     t=np.arange(0,T-1/fs,1/fs)
#     f=np.arange(0,fs-1/T,1/T)
#     y=np.loadtxt(filename)
#     ss=np.fft.fft(y) 
#     s=2*abs(ss**2)/len(t)
#     plt.figure(figsize=[22,5])
#     plt.subplot(2,1,1)
#     plt.plot(t,y)
#     plt.xlabel('t,c')
#     plt.ylabel('f(t)')
#     plt.title('Сигнал')
#     plt.grid()
#     plt.subplot(2,1,2)
#     plt.stem(f,s)
#     plt.title('Спектральна густина потужності сигналу')
#     plt.grid(True)
#     plt.xlabel('f,Гц')

#p11+
# def cuts(t1,t2,sig,fs,T):
#     if (t1>=0)&(t1<t2)&(T>t2):
#         t=np.arange(0,T-1/fs,1/fs)
#         f=np.arange(0,fs-1/T,1/T)
        
#         N1=t1*fs
#         N2=t2*fs
        
#         cutsig=sig[N1:N2]
#         cuttime=np.arange(t[N1],t[N2],1/fs)
#         cutf=np.arange(f[N1],f[N2],1/T)
        
#         plt.figure()
#         plt.subplot(3,1,1)
#         plt.plot(cuttime,cutsig)
#         plt.title('Сигнал')
#         plt.xlabel('t,c')
#         plt.ylabel('y(t)')
        
#         s=2*np.fft.fft(cutsig)/len(cutsig)
#         amp_spectr=abs(s)
#         phase_spectr=np.angle(s)
        
#         plt.subplot(3,1,2)
#         plt.plot(cutf,amp_spectr)
#         plt.title('Амплітудний спектр сигналу')
#         plt.xlabel('f,Гц')
#         plt.ylabel('Amplitude')
#         plt.xlim([0,fs/2])
        
#         plt.subplot(3,1,3)
#         plt.plot(cutf,phase_spectr)
#         plt.title('Фазовий спектр сигналу')
#         plt.xlabel('f,Гц')
#         plt.ylabel('Phase')
#     else:
#         print('Error!')