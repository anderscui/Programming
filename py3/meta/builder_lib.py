# coding=utf-8
print('@ builderlib module starts')


class Builder:
    print('@ Builder body')

    def __init_subclass__(cls, **kwargs):
        print(f'@ Builder.init_subclasses: ({cls!r})')

        def inner_0(self):
            print(f'@ Builder.init_subclasses:inner_0 ({self!r})')

        cls.method_a = inner_0

    def __init__(self):
        super().__init__()
        print(f'@ Builder.__init__({self!r}')


def deco(cls):
    print(f'@ deco({cls!r})')

    def inner_1(self):
        print(f'@ deco:inner_1({self!r})')

    cls.method_b = inner_1

    return cls


class Descriptor:
    print('@ Descriptor body')

    def __init__(self):
        print(f'@ Descriptor.init({self!r})')

    def __set_name__(self, owner, name):
        args = (self, owner, name)
        print(f'@ Descriptor.set_name_{args!r}')

    def __set__(self, instance, value):
        args = (self, instance, value)
        print(f'@ Descriptor.set_{args!r}')

    def __repr__(self):
        return '<Descriptor instance>'


print(f'@ builderlib module ends.')
