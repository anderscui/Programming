# coding=utf-8


def averager():
    total, count = 0, 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count


co = averager()
print(next(co))
print(co.send(10))
print(co.send(30))
print(co.send(5))
