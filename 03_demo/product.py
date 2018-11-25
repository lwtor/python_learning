#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def product_test(*args):
    if args == ():
        raise TypeError('')
    sum = 1
    for num in args:
        sum *= num
    return sum

def product_mine(*args):
    print(args)
    if args is ():
        raise TypeError('lwtor type error')
    sum = 0
    text = ''
    for num in args:
        if  sum == 0:
            sum = 1
        sum *= num
        if not text == '':
            text += ' * '
            pass
        text += str(num)
    print('%s = %d' %(text, sum))
    return sum

# product(5)
# product(5, 6)
# product(5, 6, 7)
# product(5, 6, 7, 9)

# 测试
product = product_test
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
