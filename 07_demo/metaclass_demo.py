#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        # print(help(print))
        print(cls, name, bases, attrs, sep='\n')
        print(attrs)
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass = ListMetaclass):
    pass

L = MyList()
L.add(1)
print(L)
