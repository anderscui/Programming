# coding=utf-8
import re
import sys
import unicodedata
from collections import Counter
from collections.abc import Iterable, Iterator, Sequence
from decimal import Decimal
from fractions import Fraction
from random import shuffle
from typing import Any, TypeAlias, TypeVar, Hashable, Protocol

# Iterable: iter
# Iterator: iter, next

# TypeAlias: to make more visible and easier to type check.

FromTo: TypeAlias = tuple[str, str]
T = TypeVar('T')
# restricted TypeVar
NumberT = TypeVar('NumberT', float, Decimal, Fraction)
# bounded TypeVar, could be Hashable or its subtypes.
HashableT = TypeVar('HashableT', bound=Hashable)


# Protocols
class SupportsLessThan(Protocol):
    def __lt__(self, other) -> bool: ...


LT = TypeVar('LT', bound=SupportsLessThan)


RE_WORD = re.compile(r'\w+')
STOP_CODE = sys.maxunicode + 1


def columnize(seq: Sequence[str], n_cols: int = 0) -> list[tuple[str, ...]]:
    if n_cols == 0:
        n_cols = round(len(seq) ** 0.5)
    n_rows, remainder = divmod(len(seq), n_cols)
    n_rows += bool(remainder)
    return [tuple(seq[i::n_rows]) for i in range(n_rows)]


def tokenize(text: str) -> Iterator[str]:
    """
    :param text:
    """
    for m in RE_WORD.finditer(text):
        yield m.group().upper()


def name_index(start: int = 32, end: int = STOP_CODE) -> dict[str, set[str]]:
    index: dict[str, set[str]] = {}
    for ch in (chr(i) for i in range(start, end)):
        if name := unicodedata.name(ch, ''):
            for w in tokenize(name):
                index.setdefault(w, set()).add(ch)
    return index


def zip_replace(text: str, changes: Iterable[FromTo]) -> str:
    for _from, to in changes:
        text = text.replace(_from, to)
    return text


def sample(population: Sequence[T], size: int) -> list[T]:
    if size < 1:
        raise ValueError(f'size must be >= 1')
    result = list(population)
    shuffle(result)
    return result[:size]


# def mode(data: Iterable[NumberT]) -> NumberT:
#     top = Counter(data).most_common(1)
#     if top:
#         return top[0][0]
#     raise ValueError('no mode for emtpy data')


def mode(data: Iterable[HashableT]) -> HashableT:
    top = Counter(data).most_common(1)
    if top:
        return top[0][0]
    raise ValueError('no mode for emtpy data')


def top(iterable: Iterable[LT], n: int) -> list[LT]:
    ordered = sorted(iterable, reverse=True)
    return ordered[:n]


if __name__ == '__main__':
    animals = 'drake fawn heron ibex koala lynx tahr xerus yak zapus'.split()
    table = columnize(animals)
    print(table)

    print('name index')
    c_index = name_index(32, 65)
    print(c_index['SIGN'], c_index['DIGIT'])

    print('zip replace')
    l33t = [('a', '4'), ('e', '3'), ('i', '1'), ('o', '0')]
    text = 'mad skilled noob powned leet'
    print(zip_replace(text, l33t))
