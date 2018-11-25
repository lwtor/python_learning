#!/usr/bin/env python3
#! -*- coding: utf-8 -*-

def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
        return
    move(n-1,a,c,b)        #把n-1的汉诺塔从a柱移动到b柱，c柱作为中转。
    print(a, '-->', c)     #把最下方的第n个盘子从a移动到c
    move(n-1,b,a,c)        #把n-1的汉诺塔从b柱移动到c柱，a柱作为中转。

move(2, 'A', 'B', 'C')
