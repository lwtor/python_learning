#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def add(x, y, f):
    return f(x) + f(y)

x = 22
y = -19
print('x =', x, ', y =', y)
print('ads(x) + abs(y) = ', add(x, y, abs))
print('x + y = ', x + y)
