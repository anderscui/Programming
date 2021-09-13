import random
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from queue import Queue


def producer(pipeline, event):
    """Pretend getting msgs from the network"""
    while not event.is_set():
        msg = random.randint(1, 100)
        pipeline.set_message(msg, 'producer')

    print(f'producer received EXIT event, exiting...')


def consumer(pipeline, event):
    """Pretend saving msg to the db"""
    while not event.is_set() or not pipeline.empty():
        msg = pipeline.get_message('consumer')
        print(f'consumer storing msg: {msg} (queue size={pipeline.qsize()}')

    print(f'consumer received EXIT event, exiting...')


class Pipeline(Queue):
    def __init__(self):
        super().__init__(maxsize=10)

    def get_message(self, name):
        print(f'{name}: about to get from queue')
        value = self.get()
        print(f'{name}: got {value} from queue')
        return value

    def set_message(self, value, name):
        print(f'{name}: about to add {value} to queue')
        self.put(value)
        print(f'{name}: added {value} to queue')


if __name__ == '__main__':
    pipeline = Pipeline()
    event = threading.Event()
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)

        time.sleep(0.01)
        print(f'main: about to set event')
        event.set()
