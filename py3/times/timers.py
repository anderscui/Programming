# coding=utf-8
from timeit import default_timer as timer


def time_taken(f, *args):
    assert callable(f)

    start = timer()
    f(*args)
    end = timer()
    return end - start


def quick_sum(nums):
    result = sum(nums)
    print(result)
    return result


def slow_sum(nums):
    result = 0
    for n in nums:
        result += n
    print(result)
    return result


def without_args():
    result = sum(range(1000000))
    print(result)
    return result


print(time_taken(quick_sum, range(1000000)))
print(time_taken(slow_sum, range(1000000)))
print(time_taken(without_args))
