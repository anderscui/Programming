# coding=utf-8
from collections.abc import Callable
from typing import Any, NoReturn, get_type_hints


class Field:
    def __init__(self, name: str, constructor: Callable):
        if not callable(constructor) or constructor is type(None):
            raise TypeError(f'{name!r} type hint must be callable')
        self.name = name
        self.constructor = constructor

    def __set__(self, instance, value):
        if value is ...:
            value = self.constructor()
        else:
            try:
                value = self.constructor(value)
            except (TypeError, ValueError) as e:
                type_name = self.constructor.__name__
                msg = f'{value!r} is not compatible with {self.name}:{type_name}'
                raise TypeError(msg) from e
        instance.__dict__[self.name] = value


class Checked:
    @classmethod
    def _fields(cls) -> dict[str, type]:
        return get_type_hints(cls)

    def __init_subclass__(subclass, **kwargs):
        super().__init_subclass__()

        subclass.__defaults__ = {}
        for name, ctor in subclass._fields().items():
            # create an attrib on `subclass` class
            print(f'add cls descriptor: {subclass} {name} {ctor}')

            try:
                default_value = getattr(subclass, name)
                subclass.__defaults__[name] = default_value
            except:
                pass

            setattr(subclass, name, Field(name, ctor))
        # print(subclass.__defaults__)

    def __init__(self, **kwargs):
        for name in self._fields():
            if name in kwargs:
                value = kwargs.pop(name)
            elif name in self.__class__.__defaults__:
                value = self.__class__.__defaults__[name]
            else:
                value = ...

            # value = kwargs.pop(name, ...)

            # trigger Checked.__setattr__
            setattr(self, name, value)
        if kwargs:
            self._flag_unknown_attrs(*kwargs)

    def __setattr__(self, name, value):
        if name in self._fields():
            cls = self.__class__
            descriptor = getattr(cls, name)
            descriptor.__set__(self, value)
        else:
            self._flag_unknown_attrs(name)

    def __repr__(self):
        kwargs = ', '.join(f'{k}={v!r}' for k, v in self._as_dict().items())
        return f'{self.__class__.__name__}({kwargs})'

    def _flag_unknown_attrs(self, *names: str):
        plural = 's' if len(names) > 1 else ''
        extra = ', '.join(f'{name!r}' for name in names)
        cls_name = repr(self.__class__.__name__)
        raise AttributeError(f'{cls_name} object has not attribute{plural}: {extra}')

    def _as_dict(self) -> dict[str, Any]:
        return {name: getattr(self, name)
                for name, attr in self.__class__.__dict__.items()
                if isinstance(attr, Field)}


class Movie(Checked):
    title: str
    year: int
    # TODO: why the order changed?
    box_office: float = 1.0


if __name__ == '__main__':
    movie = Movie()
    print(movie)

    movie = Movie(title='Before Sunrise',
                  box_office=1000,
                  year=1995)
    print(movie)
