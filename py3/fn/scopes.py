# coding=utf-8
b = 6


def f(a):
    print(a)
    print(b)


def f2(a):
    # print(locals(), 'b' in globals())
    print(a)
    print(b)
    b = 1


def f3(a):
    global b
    print(a)
    print(b)
    b = 1


if __name__ == '__main__':
    f(3)
    # error: UnboundLocalError: cannot access local variable 'b' where it is not associated with a value
    # f2(3)
    f3(3)
