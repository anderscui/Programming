# coding=utf-8
import json
import keyword
from collections import abc


class FrozenJSON:
    """A read-only facade for navigating a JSON-like object using attr notation"""
    def __init__(self, mapping):
        self._data = {}
        for k, v in mapping.items():
            if keyword.iskeyword(k):
                k += '_'
            self._data[k] = v

    def __getattr__(self, name):
        try:
            return getattr(self._data, name)
        except AttributeError:
            return FrozenJSON.build(self._data[name])

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
    # raw_feed = json.load(open('../data/osconfeed.json'))
    # feed = FrozenJSON(raw_feed)
    # # original attribs
    # print(feed.keys())
    # print(len(feed.Schedule.speakers))
    # print(feed.Schedule.keys())
    # for k, v in feed.Schedule.items():
    #     print(f'{len(v):3} {k}')
    #
    # # list as list
    # print(feed.Schedule.speakers[-1].name)
    # talk = feed.Schedule.events[40]
    # print(type(talk), talk.name, talk.speakers)

    # special keywords
    data = {'name': 'Jim Bo', 'class': 1982}
    student = FrozenJSON(data)
    # invalid syntax
    # print(student.class)
    print(student.class_)
