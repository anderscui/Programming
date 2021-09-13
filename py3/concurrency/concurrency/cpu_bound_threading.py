import time
from concurrent.futures import ThreadPoolExecutor


def cpu_bound(n):
    return sum(i * i for i in range(n))


def find_sums(nums):
    with ThreadPoolExecutor() as executor:
        executor.map(cpu_bound, nums)


if __name__ == '__main__':
    numbers = [5_000_000 + x for x in range(20)]
    start = time.time()
    find_sums(numbers)
    elapsed = time.time() - start
    # time elapsed: 7.794579982757568 seconds
    print(f'time elapsed: {elapsed} seconds')
