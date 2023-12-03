# coding=utf-8
from collections import UserDict, Counter


def _upper(key):
    try:
        return key.upper()
    except AttributeError:
        return key


class UpperCaseMixin:
    def __setitem__(self, key, value):
        super().__setitem__(_upper(key), value)

    def __getitem__(self, key):
        return super().__getitem__(_upper(key))

    def get(self, key, default=None):
        return super().get(_upper(key), default)

    def __contains__(self, key):
        return super().__contains__(_upper(key))


class UpperDict(UpperCaseMixin, UserDict):
    pass


class UpperCounter(UpperCaseMixin, Counter):
    """Specialized `Counter` impl. No `pass`."""


if __name__ == '__main__':
    d = UpperDict([('a', 'letter a'), (2, 'digit two')])
    print(list(d.keys()))  # ['A', 2]

    d['b'] = 'letter B'
    print(list(d.keys()))
    assert 'b' in d

    c = UpperCounter('BaNanA')
    print(c.most_common())
