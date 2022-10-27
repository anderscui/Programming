# coding=utf-8
from functools import wraps


def singleton(cls):
    instances = {}

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton
class OnlyOne:
    pass


if __name__ == '__main__':
    inst1 = OnlyOne()
    inst2 = OnlyOne()
    assert inst1 == inst2
