# coding=utf-8
from collections import namedtuple
from functools import reduce, partial
from operator import mul, itemgetter, attrgetter


def factorial(n):
    return reduce(mul, range(1, n+1))


LatLon = namedtuple('LatLon', 'lat lon')
Metropolis = namedtuple('Metropolis', 'name cc pop coord')


if __name__ == '__main__':
    print(factorial(5))

    metro_data = [
        ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
        ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
        ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
        ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
        ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
    ]
    for city in sorted(metro_data, key=itemgetter(1)):
        print(city)

    # # get by multiple keys
    # for city in metro_data:
    #     print(itemgetter(1, 0)(city))
    metro_areas = [Metropolis(name, cc, pop, LatLon(lat, lon))
                   for name, cc, pop, (lat, lon) in metro_data]
    print(metro_areas[0])

    print('sort by attrs')
    name_lat = attrgetter('name', 'coord.lat')
    for city in sorted(metro_areas, key=attrgetter('coord.lat')):
        print(name_lat(city))

    # partial
    triple = partial(mul, 3)
    print(triple.func, triple.args, triple.keywords)
    print([triple(i) for i in range(3)])
