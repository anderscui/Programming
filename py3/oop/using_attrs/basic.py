# coding=utf-8
import attr


class A:
    def __init__(self, a):
        self.a = a

    def __eq__(self, other):
        return self.a == other.a


@attr.s
class SomeClass:
    # attrib
    a_number = attr.ib(default=1)
    list_of_nums = attr.ib(factory=list)

    def hard_math(self, another):
        return self.a_number + sum(self.list_of_nums) * another


if __name__ == '__main__':
    sc = SomeClass(1, [1, 2, 3])
    print(sc)
    print(sc.hard_math(3))
    print(sc == SomeClass(1, [1, 2, 3]))
    print(dir(sc))

    a1 = A(1)
    a2 = A(1)
    # need __eq__
    # print(a1 == a2)

    # for namedtuple, namedtuple is not a regular type
    C1 = attr.make_class('C1', ['a'])
    print(type(C1))
    print(C1(a=1))
