import multiprocessing
import time


def cpu_bound(n):
    return sum(i * i for i in range(n))


def find_sums(nums):
    with multiprocessing.Pool() as pool:
        pool.map(cpu_bound, nums)


if __name__ == '__main__':
    numbers = [5_000_000 + x for x in range(20)]
    start = time.time()
    find_sums(numbers)
    elapsed = time.time() - start
    # time elapsed: 1.6001529693603516 seconds
    print(f'time elapsed: {elapsed} seconds')
