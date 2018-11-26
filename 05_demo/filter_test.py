#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce

# ---- 第一次写的，只想着用int做比较，思维僵化了 -_-！  ----

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def up_size_down(n):
    s = str(n)[::-1]
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

def is_palindrome_1(n):
    return n == up_size_down(n)

# ---- 直接比较字符串就可以了 ----
def is_palindrome_2(n):
    return str(n) == str(n)[::-1]

# 测试:
is_palindrome = is_palindrome_2
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

print(up_size_down(100))
