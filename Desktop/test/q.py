from scipy import *
from pylab import *

x = r_[0:50]
y1 = sin(2*pi*x/49)
#y2 = cos(2*pi*x/49)
y2 = np.zeros((y1.shape))
for i in range(15,25):
       y2[i] = 0.9
#print len(y1),len(y2)
#y3 = convolve(y2,y1,mode="same")
y3 = convolve(y2,y1)
subplot(2,2,1)
plot(x,y1)
hold(True)
plot(x,y2)
hold(True)
subplot(2,2,2)
print len(x),len(y3)
xx = r_[0:len(y3)]
print len(xx),len(y3)
plot(xx,y3)
hold(True)
show()