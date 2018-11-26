#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def func(n):
    return n % 10

print(sorted([36, 5, -12, 9, -21]))
print(sorted([36, 5, -12, 9, -21], key=abs))
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))

print(sorted([2,334,58, 43, 32, 45, 79,], key=func))
