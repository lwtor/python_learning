#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from types import MethodType

class Student(object):
    pass

s = Student()
print(dir(s))
s.name = 'lwtor'
print(dir(s))
print(s.name)

def say_hello(self):
    print('hello, I am %s' %(self.name))

s.say_hello = MethodType(say_hello, s)
s.say_hello()

Student.say_hello = say_hello
Student.name = ''

s2 = Student()
s2.name = 'allen'
s2.say_hello()

class Animal(object):
    __slots__ = ('name', 'age')

a1 = Animal()
a1.name = "cat"
a1.age = 18
print(dir(Animal))
print(a1.name, a1.age)
