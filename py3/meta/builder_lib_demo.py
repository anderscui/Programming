# coding=utf-8
# import builder_lib
from meta.builder_lib import deco, Builder, Descriptor

print('# demo module start')


@deco
class Klass(Builder):
    print('# Klass body')

    attr = Descriptor()

    def __init__(self):
        super().__init__()
        print(f'# Klass.init({self!r})')

    def __repr__(self):
        return '<Klass instance>'


def main():
    obj = Klass()
    obj.method_a()
    obj.method_b()
    obj.attr = 1


if __name__ == '__main__':
    main()
