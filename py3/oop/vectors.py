# coding=utf-8
from array import array
import math
from typing import SupportsComplex, SupportsAbs


class Vector2d:
    __match_args__ = ('x', 'y')

    # a class attrib, for conversion from/to bytes
    typecode = 'd'

    def __init__(self, x, y):
        # _x is protected
        # __x is private
        self.__x = float(x)
        self.__y = float(y)

    @classmethod
    def from_bytes(cls, octets):
        # cls: is a `type`
        type_code = chr(octets[0])
        memv = memoryview(octets[1:]).cast(type_code)
        return cls(*memv)

    @classmethod
    def from_complex(cls, datum: SupportsComplex) -> "Vector2d":
        c = complex(datum)
        return cls(c.real, c.imag)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        # make this type iterable, here use a generator
        return (val for val in (self.__x, self.__y))

    def __repr__(self):
        cls_name = type(self).__name__
        return '{}({!r}, {!r})'.format(cls_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    def __eq__(self, other: "Vector2d"):
        return tuple(self) == tuple(other)

    def __abs__(self) -> float:
        return math.hypot(self.__x, self.__y)

    def __bool__(self):
        return bool(abs(self))

    def angle(self):
        return math.atan2(self.__y, self.__x)

    def __format__(self, format_spec=''):
        if format_spec.endswith('p'):
            format_spec = format_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, format_spec) for c in coords)
        return outer_fmt.format(*components)

    def __hash__(self):
        # hash of a tuple with the components
        return hash((self.x, self.y))

    def __complex__(self) -> complex:
        return complex(self.x, self.y)


def show_vector_keywords(v: Vector2d):
    match v:
        case Vector2d(x=0, y=0):
            print(f'{v!r} is null')
        case Vector2d(x=0):
            print(f'{v!r} is vertical')
        case Vector2d(y=0):
            print(f'{v!r} is horizontal')
        case Vector2d(x=x, y=y) if x == y:
            print(f'{v!r} is diagonal')
        case _:
            print(f'{v!r} is awesome')


def show_vector_positional(v: Vector2d):
    match v:
        case Vector2d(0, 0):
            print(f'{v!r} is null')
        case Vector2d(0):
            print(f'{v!r} is vertical')
        case Vector2d(_, 0):
            print(f'{v!r} is horizontal')
        case Vector2d(x, y) if x == y:
            print(f'{v!r} is diagonal')
        case _:
            print(f'{v!r} is awesome')


if __name__ == '__main__':
    v1 = Vector2d(3, 4)
    print(v1.x, v1.y)
    x, y = v1
    assert x == v1.x and y == v1.y
    print(str(v1), repr(v1))

    v2 = eval(repr(v1))
    assert v1 == v2

    octets = bytes(v1)
    print(octets)

    v2 = Vector2d.from_bytes(octets)

    assert abs(v1) == 5.0
    assert bool(v1)
    assert not bool(Vector2d(0, 0))

    # formatting
    print(format(v1, '.2f'), format(v1, '.2fp'))
    print(hash(v1))

    v2 = Vector2d(3.1, 4.2)
    print({v1, v2})

    print('\nkeyword patterns:')
    show_vector_keywords(Vector2d(0, 0))
    show_vector_keywords(Vector2d(0, 1))
    show_vector_keywords(Vector2d(1, 1))
    show_vector_keywords(v1)

    print('\npositional patterns:')
    show_vector_positional(Vector2d(0, 0))
    show_vector_positional(Vector2d(0, 1))
    show_vector_positional(Vector2d(1, 1))
    show_vector_positional(v1)

    # private vars
    print(v1.__dict__)
    # print(v1.__x) -> error
    print(v1._Vector2d__x)  # still ok

    # complex
    v = Vector2d(3, 4)
    print(isinstance(v, SupportsComplex), isinstance(v, SupportsAbs))
