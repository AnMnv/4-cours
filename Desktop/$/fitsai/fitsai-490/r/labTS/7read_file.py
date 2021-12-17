
import json;
import matplotlib.pyplot as plt
from matplotlib import rc

rc('text', usetex=True)
rc('text.latex',unicode=True)
rc('text.latex',preamble='\usepackage[utf8]{inputenc}')
rc('text.latex',preamble='\usepackage[russian]{babel}')

def read_f(name):
    with open(name) as json_file:
        data = json.load(json_file)
        return [data['x'], data['y'], data['A']];

[x, y, A] = read_f('data.txt')
plt.plot(x, y, A, 'm')
plt.xlabel(u'Час, с')
plt.ylabel(u'Амплітуда')
plt.title(u'Iмпульс прочитаний з файлу')
plt.grid(True)
axes = plt.gca()
axes.set_xlim([-10,111])
axes.set_ylim([-1,A+1])
plt.show()
