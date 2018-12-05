#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fn(self, name='World'):
    print('Hello %s' %name)

Hello = type('Hello', (object, ), dict(hello = fn))

h = Hello()
h.hello()
