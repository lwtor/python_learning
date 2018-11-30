#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100 !')
        self._score = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0 or value > 100:
            raise ValueError('you are not a human')
        self._age = value

    @property
    def hello(self):
        print('hello')

s1 = Student()
s1.score = 70
print(s1.score)
# s1.age = -1
s1.age = 18
print(s1.age)
s1.hello = 10
