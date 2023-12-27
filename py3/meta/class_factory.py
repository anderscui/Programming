# coding=utf-8
from collections.abc import Iterable, Iterator
from typing import Any

FieldNames = str | Iterable[str]


def parse_identifiers(names: FieldNames):
    if isinstance(names, str):
        names = names.replace(',', ' ').split()
    if not all(name.isidentifier() for name in names):
        raise ValueError(f'`names` are expected to be valid identifiers: {names}')
    return tuple(names)


def record_factory(cls_name, field_names: FieldNames) -> type[tuple]:
    slots = parse_identifiers(field_names)

    def __init__(self, *args, **kwargs):
        attrs = dict(zip(self.__slots__, args))
        attrs.update(kwargs)
        for name, value in attrs.items():
            setattr(self, name, value)

    def __iter__(self) -> Iterator[Any]:
        for name in self.__slots__:
            yield getattr(self, name)

    def __repr__(self):
        values = ', '.join(f'{name}={value!r}' for name, value in zip(self.__slots__, self))
        cls_name = self.__class__.__name__
        return f'{cls_name}({values})'

    cls_attrs = dict(
        __slots__=slots,
        __init__=__init__,
        __iter__=__iter__,
        __repr__=__repr__
    )

    return type(cls_name, (object,), cls_attrs)


if __name__ == '__main__':
    Dog = record_factory('Dog', 'name weight owner')
    qing = Dog('Qing', 10, owner='ge')
    print(qing)
    name, weight, _ = qing
    print(name, weight)
    qing.weight = 11
    print(qing)
    print(Dog.__mro__)
