#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    print('try')
    t = 10 / 0
    # a = int('a')
except ZeroDivisionError as e:
    print('exception:', e)
else:
    print('no exception')
finally:
    print('finnally')
print('End')
