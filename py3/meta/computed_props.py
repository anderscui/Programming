# coding=utf-8
import json

JSON_PATH = '../data/osconfeed.json'


class Record:
    def __init__(self, **kwargs):
        # extend attributes.
        self.__dict__.update(kwargs)

    def __repr__(self):
        return f'<{self.__class__.__name__} serial={self.serial!r}>'


def load(path=JSON_PATH):
    records = {}
    with open(path) as f:
        raw_data = json.load(f)
    print('raw keys:', raw_data['Schedule'].keys())
    for collection, raw_records in raw_data['Schedule'].items():
        record_type = collection.removesuffix('s')
        for raw_record in raw_records:
            key = f'{record_type}.{raw_record["serial"]}'
            records[key] = Record(**raw_record)
    return records


if __name__ == '__main__':
    records = load()
    speaker = records['speaker.3471']
    print(speaker)
    print(speaker.name, speaker.twitter)
