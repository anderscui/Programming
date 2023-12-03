# coding=utf-8
import itertools

from toolz import take


class ArithmeticProgression:
    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end

    def __iter__(self):
        value_type = type(self.begin + self.step)
        cur = value_type(self.begin)
        i = 0
        while self.end is None or cur < self.end:
            yield cur

            # avoid the cumulative effect of floating point errors.
            i += 1
            cur = self.begin + self.step * i


def aritprog_gen(begin, step, end=None):
    """ArithmeticProgression is used to generate a iterator,
    So here use a generator function."""
    value_type = type(begin + step)
    cur = value_type(begin)
    i = 0
    while end is None or cur < end:
        yield cur

        # avoid the cumulative effect of floating point errors.
        i += 1
        cur = begin + step * i


if __name__ == '__main__':
    from fractions import Fraction
    from decimal import Decimal

    ap = ArithmeticProgression(0, 1, end=3)
    print(list(ap))

    ap = ArithmeticProgression(1, .5, 3)
    print(list(ap))

    ap = ArithmeticProgression(0, 1/3, 1)
    print(list(ap))

    ap = ArithmeticProgression(0, Fraction(1, 3), 1)
    print(list(ap))

    ap = ArithmeticProgression(0, Decimal('.1'), .3)
    print(list(ap))

    ap_gen = aritprog_gen(0, 1, 3)
    print(list(ap_gen))

    # use std lib
    gen = itertools.count(1, .5)
    print(list(take(5, gen)))

    print(list(itertools.takewhile(lambda n: n < 3, itertools.count(1, .5))))
