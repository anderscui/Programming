# coding=utf-8
from typing import NamedTuple


class City(NamedTuple):
    continent: str
    name: str
    country: str


def match_asian_cities():
    results = []
    for city in cities:
        match city:
            case City(continent='Asia'):
                results.append(city)
    return results


def match_asian_countries():
    results = []
    for city in cities:
        match city:
            case City(continent='Asia', country=cc):
                results.append(cc)
    return results


def match_asian_countries_pos():
    results = []
    for city in cities:
        match city:
            # use positional matching
            # check __match_args__
            case City('Asia', _, country):
                results.append(country)
    return results


def show_areas(areas):
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
    for record in areas:
        match record:
            case [str(name), *_, (lat, lon)] if lon <= 0:
                print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')


if __name__ == '__main__':
    cities = [
        City('Asia', 'Tokyo', 'JP'),
        City('Asia', 'Delhi', 'IN'),
        City('North America', 'Mexico City', 'MX'),
        City('North America', 'New York', 'US'),
        City('South America', 'São Paulo', 'BR'),
    ]
    print('Asian cities:', match_asian_cities())
    print('Asian countries:', match_asian_countries())
    print('Asian countries:', match_asian_countries_pos())

    metro_areas = [
        ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
        ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
        ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
        ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
        ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
    ]
    show_areas(metro_areas)
