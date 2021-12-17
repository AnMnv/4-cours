# !/usr/bin/env python
# coding=utf8

A = int(input())
F = 1
for i in range(1, A+1):
    F = F*i
    print("factorial", A, "is", F)
