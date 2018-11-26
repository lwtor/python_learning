#!/usr/bin/env python3
# -*- coding: utf-8 -*-

l = (i for i in range(100))

for i in range(0, 10):
    print(next(l))

def fun_a(x):
    print('fun a:' + str(x))
    return x % 2 == 0

def fun_b(x):
    print('fun b:' + str(x))
    return x % 3 == 0

tmp = filter(fun_a, l)
tmp = filter(fun_b, tmp)
print('---- 1 ----')

# print(list(tmp

for i in range(0, 10):
    # 通过打印可以发现，在next()方法执行的时候，序列会通过上面添加的两个过滤方法来判断该元素是否可以被得到
    print(next(tmp))
