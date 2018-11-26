#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def is_odd(n):
    return n % 2 == 0

l = range(1, 11)
print(list(filter(is_odd, l)))

# 打印素数

# 生成奇数的惰性序列
def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n

# 过滤函数
def _not_divisible(n):
    return lambda x : x % n > 0

def _not_divisible_test(num, mul):
    return num % mul > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        # 每次找到一个素数之后，就向序列中添加一个过滤函数，过滤的依据就是后续的元素不是当前元素的倍数
        it = filter(_not_divisible(n), it)

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
for n in primes():
    if n < 20:
        print(n)
    else:
        break
