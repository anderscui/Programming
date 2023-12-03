# coding=utf-8
def sub_gen():
    yield 1.1
    yield 1.2
    return 'sub gen done.'


def gen():
    yield 1
    result = yield from sub_gen()
    print('<--', result)
    yield 2


def simple_chain(*iterables):
    for i in iterables:
        yield from i


if __name__ == '__main__':
    for x in gen():
        print(x)

    print('\nchain:')
    print(list(simple_chain('abc', range(3))))
