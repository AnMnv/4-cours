
import matplotlib.pyplot

Fd = 256.0
time_min = 0
time_max = 10
A = 5
b = 0.3
a = 4.0 - b/2;

data = [[],[]];
t = time_min;
while t<=time_max:
    data[0].append(t);
    if t < a:
        data[1].append(0);
    elif t < a+b:
        data[1].append(A);
    else:
        data[1].append(0);
    t += 1.0/Fd;

matplotlib.pyplot.plot(data[0], data[1], 'g')
matplotlib.pyplot.xlabel('Time, s')
matplotlib.pyplot.ylabel('Amplitude')
matplotlib.pyplot.title('Square signal')
matplotlib.pyplot.grid(True)
axes = matplotlib.pyplot.gca()
axes.set_xlim([-1,11])
axes.set_ylim([-1,6])
matplotlib.pyplot.show()
