#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce

# ---------------------------------------

def normalize(name):
    return name[0].upper() + name[1:].lower()

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# ---------------------------------------

def prod(L):
    def multiply(x, y):
        return x * y
    return reduce(multiply, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

# ---------------------------------------

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def f_deca(x, y):
    return x * 10 + y

def f_deci(x, y):
    if x > 1:
        x = x * 0.1
    num = x * 0.1 + y * 0.1
    return num

def str2float(s):
    num_list = s.split('.')
    front = reduce(f_deca, map(char2num, num_list[0]))
    behind = reduce(f_deci, map(char2num, num_list[1][::-1]))
    return front + behind

test_list = ['1', '2', '3', '4']
print(str2float('123.456'))

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
