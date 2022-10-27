# coding=utf-8


class A:
    def who(self):
        print('A', end='')


class B(A):
    def who(self):
        super(B, self).who()
        print('B', end='')


class C(A):
    def who(self):
        super(C, self).who()
        print('C', end='')


class D(B, C):
    def who(self):
        super(D, self).who()
        print('D', end='')


if __name__ == '__main__':
    print(D.mro())
    # super() is the next element in mro.
    item = D()
    item.who()
