# coding=utf-8


class Base:

    def f1(self):
        return 'base'


def get_value(self, val: int):
    return self.factor * val


MyClass = type('MyClass',
               (Base,),
               {'factor': 2,
                'get_value': get_value})


if __name__ == '__main__':
    c = MyClass()
    print(c.factor)
    print(c.get_value(3))
