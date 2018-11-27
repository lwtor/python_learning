#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import partial

int2 = partial(int, base=2)
print(int2('1000000'))
print(int2('1010101'))

print_line = partial(print, '------------------------')
print_line()

p_start = partial(print, sep='***')
p_start('hello', 'world')
