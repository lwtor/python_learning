#!/usr/bin/env pthon3
# -*- coding: utf-8 -*-

num = int(input('input number: '))
sum = 0

for i in range(num + 1):
    sum += i
print('%d! = %d' %(num, sum))
