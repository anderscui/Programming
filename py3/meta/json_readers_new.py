# coding=utf-8
import json
import keyword
from collections import abc


class FrozenJSON:
    """A read-only facade for navigating a JSON-like object using attr notation"""
    def __new__(cls, arg):
        print(f'__new__, arg type: {type(arg)}',)
        if isinstance(arg, abc.Mapping):
            return super().__new__(cls)
        elif isinstance(arg, abc.MutableSequence):
            return [cls(item) for item in arg]
        else:
            return arg

    def __init__(self, mapping):
        print('__init__')
        self._data = {}
        for k, v in mapping.items():
            if keyword.iskeyword(k):
                k += '_'
            self._data[k] = v

    def __getattr__(self, name):
        try:
            return getattr(self._data, name)
        except AttributeError:
            return FrozenJSON(self._data[name])

    def __dir__(self):
        return self._data.keys()

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj


if __name__ == '__main__':
    # special keywords
    data = {'name': 'Jim Bo', 'class': 1982}
    student = FrozenJSON(data)
    # invalid syntax
    # print(student.class)
    print(student.class_)
