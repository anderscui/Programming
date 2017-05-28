# coding=utf-8
# Python Concurrency: https://www.youtube.com/watch?v=MCs5OvhV9S4
# A lecture of David Beazley


def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(1))
print(fib(20))
print(fib(30))
