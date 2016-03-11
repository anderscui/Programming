import re


def memo(f):
    """
    Memoize function f.
    """
    table = {}

    def fmemo(*args):
        if args not in table:
            print('calc {}'.format(args))
            table[args] = f(*args)
        return table[args]

    fmemo.memo = table
    return fmemo


def f1(n):
    return n*2


@memo
def f2(n):
    return n**2


f2(1)
f2(2)
f2(1)
