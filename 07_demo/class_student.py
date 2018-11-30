#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    count = 0

    def __init__(self, name, age = 1, gender = 'male'):
        Student.count += 1
        self.name = name
        self.__age = age
        self.__gender = gender

    def say_hello(self):
        print('hello, I am %s' %(self.name))

    def get_age(self):
        return self.__age

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender

s1 = Student('lwtor', 18)
s1.say_hello()
print(s1.get_age())
print(s1._Student__age)
print(s1.get_gender())
s1.set_gender('female')
print(s1.get_gender())

print('--------------------------')

print(s1.count)
s2 = Student('allen', 10)
print(s1.count)

Student.count = 0

# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')

print('--------------------------')
# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
