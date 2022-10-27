# coding=utf-8
from functools import wraps


def do_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper


def do_twice2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper


def repeat(n_times: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            value = None
            for _ in range(n_times):
                value = func(*args, **kwargs)
            return value

        return wrapper

    return decorator


@do_twice
def say_hi(greeting):
    print(greeting)


@do_twice2
def say_hi2(greeting):
    print(greeting)


@repeat(3)
def say_hi3(greeting):
    print(greeting)


if __name__ == '__main__':
    # print(print.__name__)
    print(say_hi.__name__)  # wrapper
    # say_hi('hi')

    print(say_hi2.__name__)  # say_hi2
    # say_hi2('hi')

    print(say_hi3.__name__)  # say_hi3
    say_hi3('hi')
