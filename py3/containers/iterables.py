# coding=utf-8
from collections.abc import Iterable
from random import randint


class Spam:
    def __getitem__(self, item):
        print(f'->{item}')
        raise IndexError


class GooseSpam:
    def __iter__(self):
        pass


def d6():
    return randint(1, 6)


if __name__ == '__main__':
    spam_can = Spam()
    print(iter(spam_can))  # is iterable (__iter__ or getitem)
    print(isinstance(spam_can, Iterable))  # but not Iterable

    goose_spam = GooseSpam()
    # print(iter(goose_spam))  # not iterable
    print(issubclass(GooseSpam, Iterable), isinstance(goose_spam, Iterable))  # but Iterable

    d6_iter = iter(d6, 1)
    print(type(d6_iter), list(d6_iter))

    # a manual `for` loop
    s = 'abc'
    it = iter(s)
    while True:
        try:
            print(next(it), end=' ')
        except StopIteration:
            del it
            break
