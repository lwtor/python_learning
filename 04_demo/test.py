#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a=['a','b','c','d','e','f','g','h','i','j','k']
for x in a:
    print('for: ', x)
    print(a.pop(2))
print('a=',a)#['a','b','i','j','k']为什么ijk没有被弹出
n=a.pop(2)
print('x=',x)#x是k，
print('n=',n)#n是i,pop(2)为什么是i
