#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fact(num):
    if num == 1:
        return 1
    return fact(num - 1) * num

# 使用尾递归
# 然而python并没有对尾递归做优化。。。
def fact_good(num):
    return fact_real(num, 1)

def fact_real(num, product):
    if num == 1:
        return product
    return fact_real(num - 1 , num * product)

num = input('input num: ')

print('result: ' + str(fact_good(int(num))))
