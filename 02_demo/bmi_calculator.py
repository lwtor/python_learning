#!/usr/bin/env python3
# -*- coding: utf-8 -*-

height = float(input('input your height(m): '))
weight = float(input('input your weight(kg): '))

bmi_value = weight / (height * height)
print('bmi value : %.2f' %(bmi_value))
if bmi_value < 18.5:
    print('<18.5 --> 过轻')
elif bmi_value < 23:
    print('18.5 ~ 23 --> 正常')
elif bmi_value < 32:
    print('23 ~ 32 --> fat')
else:
    print('<32 --> very fat')
