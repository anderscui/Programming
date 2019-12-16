# coding=utf-8
import time
import threading


def wait_and_print(msg):
    time.sleep(1.0)
    print(msg)


def wait_and_print_async(msg):
    def callback():
        time.sleep(1)
        print(msg, flush=True)

    timer = threading.Timer(0.0, callback)
    timer.start()


start = time.time()
wait_and_print_async('First')
wait_and_print_async('Second')
wait_and_print_async('Third')

time.sleep(1.1)
print(time.time() - start)
