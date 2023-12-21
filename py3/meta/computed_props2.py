# coding=utf-8
import inspect
import json
from functools import cache

JSON_PATH = '../data/osconfeed.json'


class Record:

    __index = None

    def __init__(self, **kwargs):
        # extend attributes.
        self.__dict__.update(kwargs)

    def __repr__(self):
        return f'<{self.__class__.__name__} serial={self.serial!r}>'

    @staticmethod
    def fetch(key):
        if Record.__index is None:
            Record.__index = load()
        return Record.__index[key]


class Event(Record):
    def __repr__(self):
        try:
            return f'<{self.__class__.__name__} {self.name!r}>'
        except AttributeError:
            return super().__repr__()

    @property
    def venue(self):
        key = f'venue.{self.venue_serial}'
        # here, use `__class__` instead of `self`
        return self.__class__.fetch(key)

    @property
    @cache
    def speakers(self):
        spkr_serials = self.__dict__.get('speakers', [])
        fetch = self.__class__.fetch
        print('fetching speakers...')
        return [fetch(f'speaker.{key}') for key in spkr_serials]


def load(path=JSON_PATH):
    records = {}
    with open(path) as f:
        raw_data = json.load(f)
    print('raw keys:', raw_data['Schedule'].keys())
    for collection, raw_records in raw_data['Schedule'].items():
        record_type = collection.removesuffix('s')
        cls_name = record_type.capitalize()
        cls = globals().get(cls_name, Record)
        if inspect.isclass(cls) and issubclass(cls, Record):
            factory = cls
        else:
            factory = Record

        for raw_record in raw_records:
            key = f'{record_type}.{raw_record["serial"]}'
            records[key] = factory(**raw_record)

    return records


if __name__ == '__main__':
    event = Record.fetch('event.33950')
    print(event)
    print(event.venue)
    print(event.venue.name, event.venue_serial)
    print('\ntest cache...')
    for i in range(3):
        for speaker in event.speakers:
            print('speaker:', speaker)
        print()
