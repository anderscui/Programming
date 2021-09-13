import time


def cpu_bound(n):
    return sum(i * i for i in range(n))


def find_sums(nums):
    for n in nums:
        cpu_bound(n)


if __name__ == '__main__':
    numbers = [5_000_000 + x for x in range(20)]
    start = time.time()
    find_sums(numbers)
    elapsed = time.time() - start
    # time elapsed: 7.635008096694946 seconds
    print(f'time elapsed: {elapsed} seconds')
