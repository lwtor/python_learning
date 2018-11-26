#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def func(x):
    return x * x

l = range(1, 11)
print(list(map(func, l)))
print(list(map(str, l)))

print(list(func(x) for x in l))

test = [func(x) for x in l]
print(test)
