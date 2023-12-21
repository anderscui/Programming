# coding=utf-8
import typing
from collections import namedtuple
from dataclasses import dataclass

from typing import NamedTuple


class Coordinate:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon


Coordinate2 = namedtuple('Coordinate', 'lat lon')

NamedCoordinate = NamedTuple('Coordinate', [('lat', float), ('lon', float)])


class NamedCoordinate2(NamedCoordinate):
    lat: float
    lon: float

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'


@dataclass(frozen=True)
class DataClassCoordinate:
    lat: float
    lon: float

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'


if __name__ == '__main__':
    moscow = Coordinate(55.76, 37.62)
    # useless repr
    print(moscow)
    city = Coordinate(55.76, 37.62)
    # meaningless eq.
    print(moscow == city, (moscow.lat, moscow.lon) == (city.lat, city.lon))

    assert issubclass(Coordinate2, tuple)
    moscow = Coordinate2(55.76, 37.62)
    print(moscow)
    city = Coordinate2(55.76, 37.62)
    print(moscow == city, (moscow.lat, moscow.lon) == (city.lat, city.lon))

    assert issubclass(NamedCoordinate, tuple)
    print(typing.get_type_hints(NamedCoordinate))
    moscow = NamedCoordinate(55.76, 37.62)
    print(moscow)
    city = NamedCoordinate(55.76, 37.62)
    print(moscow == city, (moscow.lat, moscow.lon) == (city.lat, city.lon))

    assert issubclass(NamedCoordinate2, tuple)
    print(typing.get_type_hints(NamedCoordinate2))
    moscow = NamedCoordinate2(55.76, 37.62)
    print(moscow)
    city = NamedCoordinate2(55.76, 37.62)
    print(moscow == city, (moscow.lat, moscow.lon) == (city.lat, city.lon))

    assert not issubclass(DataClassCoordinate, tuple)
    print(typing.get_type_hints(DataClassCoordinate))
    moscow = DataClassCoordinate(55.76, 37.62)
    print(moscow)
    city = DataClassCoordinate(55.76, 37.62)
    print(moscow == city, (moscow.lat, moscow.lon) == (city.lat, city.lon))
