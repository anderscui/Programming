# coding=utf-8
from __future__ import unicode_literals

i = iter('abc')
print(next(i))
print(next(i))
print(next(i))
print(next(i, 'exhausted'))
