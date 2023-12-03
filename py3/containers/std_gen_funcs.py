# coding=utf-8
import itertools
import operator

from toolz import take


if __name__ == '__main__':
    print(list(itertools.compress('python', (0, 1, 0, 1, 1))))

    print(list(itertools.dropwhile(lambda i: i < 5, range(10))))
    print(list(itertools.takewhile(lambda i: i < 5, range(10))))

    print(list(filter(lambda i: i % 2 == 0, range(10))))
    print(list(itertools.filterfalse(lambda i: i % 2 == 0, range(10))))

    print(list(itertools.islice(range(10), 2)))
    print(list(itertools.islice(range(10), 2, 5)))
    print(list(itertools.islice(range(10), 2, None)))
    print(list(itertools.islice(range(10), 2, None, 2)))

    print(list(itertools.accumulate([1])))
    print(list(itertools.accumulate([1, 2])))
    # factorials
    print(list(itertools.accumulate(range(1, 11), operator.mul)))

    print(list(enumerate('abc', start=1)))

    # squares
    print(list(map(operator.mul, range(5), range(5))))

    print(list(itertools.starmap(operator.mul, enumerate(range(1, 6), 1))))

    # chain
    print(list(itertools.chain('ABC', 'DEF')))
    print(list(itertools.chain.from_iterable(['ABC', 'DEF'])))

    print(list(itertools.product([1, 2])))
    print(list(itertools.product([1, 2], (3, 4, 5))))

    print(list(itertools.zip_longest([1, 2], (3, 4, 5), fillvalue=0)))

    # expand
    print(list(itertools.combinations('abc', 1)))
    print(list(itertools.combinations('abc', 2)))
    print(list(itertools.combinations('abc', 3)))
    print(list(itertools.combinations('abc', 4)))  # []

    print(list(itertools.combinations_with_replacement('abc', 2)))

    print(list(take(10, itertools.cycle('abc'))))
    print(list(itertools.islice(itertools.cycle('abc'), 10)))

    print(list(itertools.pairwise(range(6))))

    print(list(itertools.permutations('abc')))
    print(list(itertools.permutations('abc', 2)))

    print(list(itertools.repeat(1, times=5)))

    print(list(zip(*itertools.tee('abc', 2))))
    print(list(zip(*itertools.tee('abc', 3))))
