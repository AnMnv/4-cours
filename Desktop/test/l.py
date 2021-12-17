#!/usr/bin/env python
#coding=utf8
import numpy as np

A = input()
B = input()
matrix =[]
for i in range(A):
	line = []
	for j in range(B):
		line.append(input())
	matrix.append(line)
a = np.array(matrix)
print (a)   
