#!/usr/bin/env python
#coding=utf8
import json;
import matplotlib.pyplot as plt

with open('a.txt') as json_file:
    a = json.load(json_file)
    plt.plot(a['x'], a['y'], a['A'], a['color'])
    plt.xlabel('Time, s')
    plt.ylabel('Amplitude')
    plt.title('Impuls readen from file')
    plt.grid(True)
    axes = plt.gca()
    axes.set_xlim([-1,11])
    axes.set_ylim([-1,a['A']+1])
    plt.show()
