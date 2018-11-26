#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def lazy_sum(l):
    def sum():
        ax = 0
        for n in l:
            ax = ax + n
        return ax
    return sum

l = [1, 3, 5, 7, 9]

print(l)

f1 = lazy_sum(l)
print(f1())
f2 = lazy_sum(l)
print(f2())

print(f1 == f2)

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())

print('-------------')

l = [1]

def func(L):
    print('func')
    def fun():
        print('fun')
        return L[0]
    return fun

f1 = func(l)
print(f1())
l[0] = 3
print(f1())

print('-------------')

def count_1():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1, f2, f3 = count_1()
print(f1())
print(f2())
print(f3())
