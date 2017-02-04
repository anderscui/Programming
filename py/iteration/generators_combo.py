# coding=utf-8
from __future__ import unicode_literals


def power(values):
    for val in values:
        print('powering {}'.format(val))
        yield val


def adder(values):
    for val in values:
        print('adding to {}'.format(val))
        if val % 2 == 0:
            yield val + 3
        else:
            yield val + 2


nums = [1, 4, 7, 9, 12, 19]
results = adder(power(nums))
print(next(results))
print(next(results))
print(next(results))
