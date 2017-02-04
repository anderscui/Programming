# coding=utf-8
from __future__ import unicode_literals


# list
evens = [n*2 for n in range(10)]
for n in evens:
    print(n)

# set
nums = {n%2 for n in range(10)}
print(type(nums))
for n in nums:
    print(n)

# dict
squares = {n: n**2 for n in range(5)}
for n in squares:
    print('{}: {}'.format(n, squares[n]))
