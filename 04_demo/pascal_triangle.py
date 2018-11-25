#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def pascal_triangle_print(max):
    pre = [1]
    cur = []
    column = 1
    print(pre)
    while(column < max):
        length = len(pre)
        for index in range(0, length):
            pre_num = 0
            cur_num = pre[index]
            if index > 0:
                pre_num = pre[index - 1]
            cur.append(pre_num + cur_num)
            if index == len(pre) - 1:
                cur.append(cur_num)
        print(cur)
        pre = cur
        cur = []
        column += 1

def pascal_triangle_plus(max):
    pre = [1]
    cur = []
    column = 1
    print(pre)
    while(column < max):
        length = len(pre)
        cur.append(1)
        for index in range(1, length):
            cur.append(pre[index - 1] + pre[index])
        cur.append(1)
        print(cur)
        pre = cur
        cur = []
        column += 1

def triangles():
    y=[1]
    while True:
        yield y
        y=[1]+[y[i]+y[i+1]for i in range(len(y)-1)]+[1]

pascal_triangle_print(10)
pascal_triangle_plus(10)

func = triangles()
for i in range(0, 10):
    print(next(func))
