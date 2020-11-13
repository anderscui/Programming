# coding=utf-8
from dataclasses import dataclass


@dataclass
class DataClassCard:
    rank: str
    suit: str


queen_of_hearts = DataClassCard('Q', suit='Hearts')
print(queen_of_hearts)
print(queen_of_hearts == DataClassCard('Q', 'Hearts'))

# make namedtuple-like class

from dataclasses import make_dataclass

Position = make_dataclass('Position', ['name', 'lat', 'lon'])
print(Position(name='a', lat=1, lon=2))
