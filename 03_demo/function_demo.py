#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def calculation(x, y):
    return x+y, x-y

add_result, sub_result = calculation(10, 7)
print(add_result, sub_result)

tuple_result = calculation(10, 7)
print(tuple_result)

def key_parameter(x, y, **z):
    print(x, y, z)

key_parameter(1, 2)
key_parameter(1, 2, z1 = 3, z2 = 4)

extra = {'z3': 'a', 'z4': 'b'}
key_parameter(1, 2, **extra)

def func_a(x, y, *, a, b):
    print(x, y, a, b)

def func_b(x, y, a, b):
    print(x, y, a, b)

dict_a = {'a': 'dic_a', 'b': 'dic_b', 'c': 'dic_c'}
func_a(1, 2, a=3, b=4)
func_a(1, 2, **dict_a)
