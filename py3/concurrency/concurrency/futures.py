# coding=utf-8
import time
import threading
from concurrent.futures import Future


def network_request_async(n):
    future = Future()
    result = {'success': True, 'result': n ** 2}
    timer = threading.Timer(1.0, lambda: future.set_result(result))
    timer.start()
    return future


def fetch_square(n):
    fut = network_request_async(n)

    def on_done(future):
        result = future.result()
        if result['success']:
            print(f'result is {result["result"]}')

    fut.add_done_callback(on_done)


start = time.time()
fetch_square(2)
fetch_square(3)
fetch_square(4)

time.sleep(1.1)
print(time.time() - start)
