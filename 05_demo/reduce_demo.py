#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce

def func(x, y):
    return x + y

l = list(range(1, 11))
print(l)
print(reduce(func, l))

def char2num(s):
    digits = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    return digits[s]

def fn(x, y):
    return x * 10 + y
l = [1, 9, 9, 0, 1, 1, 2, 0]
print(reduce(fn,  map(char2num, '183294')))

# 使用 lambda 进行简化
def char2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

print(char2int('1233456'))

def lambda_test(f, x, y):
    return f(x, y)

print(lambda_test(lambda x, y: x + y, 10, 11))
