# coding=utf-8


def my_enumerate(iterable):
    i = 0
    for item in iterable:
        yield i, item
        i += 1


def circle(iterable, n: int):
    items = list(iterable)
    cur = 0
    while cur < n:
        yield items[cur % len(items)]
        cur += 1


if __name__ == '__main__':
    # items = [1, 2, 3]
    # print(list(enumerate(items)))
    # print(list(my_enumerate(items)))
    # print(list(my_enumerate('abcde')))

    print(list(circle('abc', 3)))
    print(list(circle('abc', 5)))
