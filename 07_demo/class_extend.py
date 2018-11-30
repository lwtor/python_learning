#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
    def run(self):
        print('animal is running')

    def eat(self):
        print('animal is eatting')

class Cat(Animal):
    def run(self):
        print('cat is running')

class Tree(object):
    def run(self):
        print('tree can\'t  run')

def call_run(animal):
    animal.run()

cat1 = Cat()
cat1.run()
cat1.eat()

call_run(Animal())
call_run(Cat())
call_run(Tree())
