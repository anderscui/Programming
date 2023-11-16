# coding=utf-8
import functools
import itertools
import operator
import reprlib
import math

from array import array


class Vector:
    __match__args__ = ('x', 'y', 'z', 't')

    typecode = 'd'

    def __init__(self, items):
        self._items = array(self.typecode, items)

    @classmethod
    def from_bytes(cls, octets):
        # cls: is a `type`
        type_code = chr(octets[0])
        memv = memoryview(octets[1:]).cast(type_code)
        return cls(memv)

    def __iter__(self):
        return iter(self._items)

    def __repr__(self):
        items = reprlib.repr(self._items)
        items = items[items.find('['):-1]
        return f'Vector({items})'

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(self._items))

    def __eq__(self, other: "Vector"):
        # inefficient
        # return tuple(self) == tuple(other)

        # if len(self) != len(other):
        #     return False
        # for a, b in zip(self, other):
        #     if a != b:
        #         return False
        # return True

        # simpler
        return len(self) == len(other) and all(a == b for a, b in zip(self, other))

    def __hash__(self):
        hashes = (hash(item) for item in self._items)
        return functools.reduce(operator.xor, hashes, 0)

    def __abs__(self):
        return math.hypot(*self)

    def __bool__(self):
        return bool(abs(self))

    # sequence protocol
    def __len__(self):
        return len(self._items)

    def __getitem__(self, index):
        if isinstance(index, slice):
            cls = type(self)
            return cls(self._items[index])

        index = operator.index(index)
        return self._items[index]

    def __getattr__(self, name):
        cls = type(self)
        try:
            pos = cls.__match__args__.index(name)
        except ValueError:
            pos = -1
        if 0 <= pos < len(self._items):
            return self._items[pos]
        msg = f'{cls.__name__!r} object has no attribute {name!r}'
        raise AttributeError(msg)

    def __setattr__(self, name, value):
        if not name.startswith('_'):
            print('set attr:', name, value)
        cls = type(self)
        if len(name) == 1:
            if name in cls.__match__args__:
                error = 'readonly attribute {attr_name!r}'
            elif name.islower():
                error = "can't set attributes 'a' to 'z' in {cls_name!r}"
            else:
                error = ''
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=name)
                raise AttributeError(msg)
        super().__setattr__(name, value)

    def angle(self, n):
        r = math.hypot(*self[n:])
        a = math.atan2(r, self[n-1])
        if (n == len(self) - 1) and (self[-1] < 0):
            return math.pi * 2 - a
        else:
            return a

    def angles(self):
        return (self.angle(n) for n in range(1, len(self)))

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('h'):
            fmt_spec = fmt_spec[:-1]
            coords = itertools.chain([abs(self)], self.angles())
            output_fmt = '<{}>'
        else:
            coords = self
            output_fmt = '({})'
        components = (format(c, fmt_spec) for c in coords)
        return output_fmt.format(', '.join(components))


if __name__ == '__main__':
    v1 = Vector((3, 4))
    print(str(v1), repr(v1))
    x, y = v1

    v2 = eval(repr(v1))
    assert v1 == v2

    octets = bytes(v1)
    print(octets)

    v2 = Vector.from_bytes(octets)
    assert v1 == v2

    v1 = Vector((3, 4, 5))
    print(len(v1), v1[0], v1[-1])

    v2 = Vector(range(7))
    print(v2[1:4], v2[-1:])
    print(v2.x, v2.y, v2.z)

    try:
        v2.a = 10
    except AttributeError as e:
        print(f'set attr error:', e)
    # print(v2.ab)

    # hashing
    v1 = Vector((3, 4))
    v2 = Vector((3.1, 4.2))
    print(hash(v1), hash(v2))

    # formatting
    print(format(v1), format(v1, '.2f'), format(v1, '.3e'))

    v2 = Vector(range(7))
    print('abs:', abs(v2))
    print(format(v2), format(v2, '.2f'), format(v2, '.3fh'))
