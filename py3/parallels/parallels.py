# coding=utf-8
from concurrent.futures import ProcessPoolExecutor
import time
from datetime import datetime

data = (
    ['a', '2'], ['b', '4'], ['c', '6'], ['d', '8'],
    ['e', '1'], ['f', '3'], ['g', '5'], ['h', '7']
)


def mp_worker(p):
    inputs, the_time = p
    print('{} waiting {} seconds'.format(inputs, the_time))
    time.sleep(int(the_time))
    print('{} done'.format(inputs))
    return inputs * int(the_time)


def mp_handler():
    result = []
    with ProcessPoolExecutor() as executor:
        for r in executor.map(mp_worker, data):
            result.append(r)
    return result


if __name__ == '__main__':
    print(datetime.now())
    res = mp_handler()
    print(res)
    print(datetime.now())
