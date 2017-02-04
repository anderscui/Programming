# coding=utf-8
from __future__ import unicode_literals


class CountDown(object):
    def __init__(self, step):
        self.step = step

    # Python 3: use __next__
    def next(self):
        if self.step <= 0:
            raise StopIteration
        self.step -= 1
        return self.step

    def __iter__(self):
        return self


if __name__ == '__main__':
    for elem in CountDown(5):
        print(elem)
