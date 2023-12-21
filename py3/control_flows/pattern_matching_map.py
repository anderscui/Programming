# coding=utf-8
from collections import OrderedDict


def get_creators(record: dict) -> list:
    match record:
        # match a name `seq`
        case {'type': 'book', 'api': 2, 'authors': [*names]}:
            return names
        case {'type': 'book', 'api': 1, 'author': name}:
            return [name]
        case {'type': 'book'}:
            raise ValueError(f'Invalid `book` record: {record!r}')
        case {'type': 'movie', 'director': name}:
            return [name]
        case _:
            raise ValueError(f'Invalid record: {record!r}')


if __name__ == '__main__':
    b1 = dict(api=1, author='Douglas Hofstadter',
              type='book', title='Gödel, Escher, Bach')
    print(get_creators(b1))

    b2 = OrderedDict(api=2, type='book',
                     title='Python in a Nutshell',
                     authors='Martelli Ravenscroft Holden'.split())
    print(get_creators(b2))

    food = dict(category='ice cream', flavor='vanilla', cost=199)
    match food:
        case {'category': 'ice cream', **details}:
            print(f'ice cream details: {details}')
