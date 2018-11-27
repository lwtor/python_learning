#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'lwtor'

import sys

__test_param__ = "test"
inner_param = "inner_param"

def hello():
    print('test param:', __test_param__)
    print('inner param:', inner_param)
    args = sys.argv
    print('arguments:', args)
    if len(args) == 1:
        print('Hello, World!!')
    elif len(args) == 2:
        print('Hello, %s!!' %(args[1]))
    else:
        print('too many arguments')

if __name__ == '__main__':
    hello()
