# coding=utf-8
import time


def network_request(n):
    time.sleep(1.0)
    return {'success': True, 'result': n ** 2}


def fetch_square(n):
    resp = network_request(n)
    if resp['success']:
        print(f'result is {resp["result"]}')


fetch_square(2)
fetch_square(3)
fetch_square(4)
