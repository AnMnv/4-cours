
import json;
import matplotlib.pyplot as plt

def chitat_json(name):
    with open(name) as json_file:
        data = json.load(json_file)
        return [data['t'], data['f'], data['amplitude']];

[t, f, amplitude] = chitat_json('1')
plt.plot(t, f, amplitude, 'r')
plt.xlabel('t')
plt.ylabel('f')
plt.show()
