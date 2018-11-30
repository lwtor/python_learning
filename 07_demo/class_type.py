#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Test(object):
    def __init__(self, a, b):
        self.__a = a
        self.b = b

t = Test('a_param', 'b_param')
print(type(t))
print(type(t) == Test)
print(type(t) == str)
print(dir(t))

print(getattr(t, 'b'))
setattr(t, 'b', 'new_b_param')
print(getattr(t, 'b'))
print(t.b)
print(hasattr(t, 'b'))
print(hasattr(t, 'a'))
