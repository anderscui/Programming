# coding=utf-8
import time
import threading


def network_request_async(n, on_done):

    def timer_done():
        on_done({'success': True, 'result': n ** 2})

    timer = threading.Timer(1.0, timer_done)
    timer.start()


def fetch_square(n):
    def on_done(result):
        if result['success']:
            print(f'result is {result["result"]}')

    network_request_async(n, on_done)


start = time.time()
fetch_square(2)
fetch_square(3)
fetch_square(4)

time.sleep(1.1)
print(time.time() - start)
