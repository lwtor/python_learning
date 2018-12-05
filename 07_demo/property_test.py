#!/usr/bin/env python3
# -*- coding; uft-8 -*-

class Screen(object):
    @property
    def width(self):
        print('get width')
        return self._width

    @width.setter
    def width(self, value):
        print('set width %d' %value)
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height

s = Screen()
s.width = 3
s.height = 2
print(s.width)
print(s.height)
print(s.resolution)

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
