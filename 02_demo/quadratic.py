#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

a = input('input the a parameter: ')
b = input('input the b parameter: ')
c = input('input the c parameter: ')

delta = math.sqrt(b * b -(4 * a * c))
print('the result %.1f, %.1f' %((-b + delta)/(2*a), (-b - delta)/(2*a)) )
