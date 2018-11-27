#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, functools

def wraps(func):
    real_name = func.__name__
    def change_name(func):
        func.__name__ = real_name
        return func
    return change_name

def metric(func):
    @wraps(func)
    def wrapper(*args, **kw):
        time_ms = time.time()
        result = func(*args, **kw)
        print('%s executed in %s ms' % (func.__name__, time.time() - time_ms))
        return result
    return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

print('fast, ', fast.__name__)
print('slow, ', slow.__name__)

f = fast(11, 22)
s = slow(11, 22, 33)
print('result', f, s)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
