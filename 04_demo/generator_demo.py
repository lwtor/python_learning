#!/usr/bin/env python3
# -*- coding: utf-8 -*-

l = [x * x for x in range(1, 10)]
g = (x * x for x in range(1, 10))

# print(l)
# print(g)

for tmp in g:
    print(tmp)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a+b
        n += 1
    return 'done'

def fib_gen(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n += 1

print('\n')

fib(6)

print('\n')

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

o = odd()
print(next(o))
print(next(o))
print(next(o))
print('---- 1 ----')
print(next(odd()))
print(next(odd()))

print('---- 2 ----')

test = fib_gen(20)
for i in test:
    print(i)
