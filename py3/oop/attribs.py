# coding=utf-8

class Parent:
    a = 1


class Child(Parent):
    pass


if __name__ == '__main__':
    p = Parent()
    c = Child()
    print(Parent.a, p.a, Child.a, c.a)
    c.a = 2
    print(Parent.a, p.a, Child.a, c.a)
