import random
import threading
from concurrent.futures import ThreadPoolExecutor

SENTINEL = object()


def producer(pipeline):
    """Pretend getting msgs from the network"""
    for i in range(10):
        msg = random.randint(1, 100)
        pipeline.set_message(msg, 'producer')

    # send a sentinel to tell consumer it's done
    pipeline.set_message(SENTINEL, 'producer')


def consumer(pipeline):
    """Pretend saving msg to the db"""
    msg = 0
    while msg is not SENTINEL:
        msg = pipeline.get_message('consumer')
        if msg is not SENTINEL:
            print(f'consumer storing msg: {msg}')


class Pipeline:
    """Allows a single element pipeline between producer and consumer."""
    def __init__(self):
        self.message = 0
        self.producer_lock = threading.Lock()
        self.consumer_lock = threading.Lock()
        self.consumer_lock.acquire()

    def get_message(self, name):
        self.consumer_lock.acquire()
        print(f'{name}: have getlock')
        message = self.message
        self.producer_lock.release()
        print(f'{name}: setlock released')
        return message

    def set_message(self, message, name):
        self.producer_lock.acquire()
        print(f'{name}: have setlock')
        self.message = message
        self.consumer_lock.release()
        print(f'{name}: getlock released')


if __name__ == '__main__':
    pipeline = Pipeline()
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline)
        executor.submit(consumer, pipeline)
