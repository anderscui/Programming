import time


class Foo(object):
    @staticmethod
    def add(x, y):
        return x + y


class Date():

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return '%d/%d/%d' % (self.month, self.day, self.year)

    @staticmethod
    def now():
        t = time.localtime()
        return Date(t.tm_year, t.tm_mon, t.tm_mday)

    @staticmethod
    def tomorrow():
        t = time.localtime(time.time() + 86400)
        return Date(t.tm_year, t.tm_mon, t.tm_mday)


if __name__ == '__main__':
    print(Foo.add(1, 2))

    print(Date(1970, 1, 15))
    print(Date.now())
    print(Date.tomorrow())