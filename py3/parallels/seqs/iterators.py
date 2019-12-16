# coding=utf-8

s = 'abc'
it = iter(s)
while True:
    try:
        print(next(it))
    except StopIteration:
        del it
        break
