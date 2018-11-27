#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 测试可接受任意参数的函数

def test(*args, **kw):
    print(*args)
    print(args)
    # print(**kw)
    print(kw)

def test_kw(**kw):
    # print(**kw)
    print(kw)

test(1, 2, 'test', a=1, b=3)
test_kw(z=1)

print('---------------------------------------------------')

# 普通的装饰器

def log(func):
    print('log', func)
    def wrapper(*args, **kw):
        wrapper.__name__ = func.__name__
        print('call %s()' %(func.__name__))
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2018-11-27')

def now_origin():
    print('2018-11-27')

f = now
f()

log(now_origin)()

@log
def print_list(L, num = 0):
    print(L, '  --  ', str(num))

print_list(list(range(0, 11)), num=104)

print('now.__name__ =', now.__name__)

print('---------------------------------------------------')

# 测试装饰器

def test_1(func):
    print('test 1')
    return test_2

def test_2():
    print('text 2')

def replace(text):
    print(text)
    return test_1

@replace('xx')
def hello():
    print('hello')

hello()
replace('yy')(hello)()

print('---------------------------------------------------')

# 包含参数的装饰器
print(1)

def log_info(text):
    print('log_info', text)
    def decorator(func):
        print('log_info$decorator', func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

print(2)

@log_info('execute')
def print_test():
    print('2018-11-27')

print(3)
print_test()
print('print_test.__name__: ', print_test.__name__)
print('end')
