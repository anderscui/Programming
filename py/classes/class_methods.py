class Times(object):
    factor = 1

    @classmethod
    def mul(cls, x):
        return cls.factor * x


class TwoTimes(Times):
    factor = 2

print(TwoTimes.mul(3))