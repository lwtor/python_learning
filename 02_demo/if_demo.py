#!/usr/bin/env python3
# -*- coding: utf-8 -*-

age = input('input your age:')
if int(age) >= 18:
  print('you are adult!!!')
elif int(age) < 0:
  print('you are liar')
else:
  print("you can't go on")
