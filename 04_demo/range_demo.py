#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os

l = list(range(1, 10))

print('range(1, 10): ', list(range(1, 10)))
print('range(4, 10): ', list(range(4, 10)))

print([x * x for x in range(1, 10)])
print(list(x * x for x in range(1, 10)))

print(list((x * x) + 1 for x in range(1, 10) if x % 2 == 0))

print(list(m + n for m in 'ABC' for n in 'XYZ'))

print(list(d for d in os.listdir('.')))

d = {'x': 'A', 'y': 'B', 'z': 'C'}
print(list(k + '=' + v for k, v in d.items()))

L = ['Hello', 'World', 18, 'Apple', None]
l = ['Hello', 'World', "Lwtor", "Allen"]
print(list(s.lower() for s in l))
print(list(s.lower() for s in L if isinstance(s, str)))
