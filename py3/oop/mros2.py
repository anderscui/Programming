# coding=utf-8


class Root:
    def ping(self):
        print(f'{self}.ping() in Root')

    def pong(self):
        print(f'{self}.pong() in Root')

    def __repr__(self):
        cls_name = type(self).__name__
        return f'<instance of {cls_name}'


class A(Root):
    def ping(self):
        print(f'{self}.ping() in A')
        super().ping()

    def pong(self):
        print(f'{self}.pong() in A')
        super().pong()


class B(Root):
    def ping(self):
        print(f'{self}.ping() in B')
        super().ping()

    def pong(self):
        print(f'{self}.pong() in B')


class Leaf(A, B):
    def ping(self):
        print(f'{self}.ping() in Leaf')
        super().ping()


class Leaf2(B, A):
    def ping(self):
        print(f'{self}.ping() in Leaf2')
        super().ping()


class U:
    def ping(self):
        print(f'{self}.ping() in U')
        super().ping()


class LeafUA(U, A):
    def ping(self):
        print(f'{self}.ping() in LeafUA')
        super().ping()


class LeafAU(A, U):
    def ping(self):
        print(f'{self}.ping() in LeafAU')
        super().ping()


if __name__ == '__main__':
    leaf = Leaf()
    # super() is the next element in mro.
    leaf.ping()
    # A, B
    leaf.pong()

    leaf2 = Leaf2()
    # B: B doesn't call super()
    leaf2.pong()

    u = U()
    # u.ping()  # 'super' object has no attribute 'ping'

    leafua = LeafUA()
    # LeafUA, U, A, Root, i.e. in this case, A is the super() of U.
    leafua.ping()

    leafau = LeafAU()
    print(LeafAU.mro())
    leafau.ping()
