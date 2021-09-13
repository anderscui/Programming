import threading
import time
from concurrent.futures import ThreadPoolExecutor


class FakeDb:
    def __init__(self):
        # shared data
        self.value = 0
        self._lock = threading.Lock()

    def update(self, name):
        print(f'thread {name}: starting update')
        print(f'thread {name}: about to lock')
        with self._lock:
            print(f'thread {name}: has lock')
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy
            print(f'thread {name}: about to release lock')

        print(f'thread {name}: after to release')
        print(f'thread {name}: finishing update')


if __name__ == '__main__':
    db = FakeDb()
    print(f'starting value is {db.value}')
    with ThreadPoolExecutor(max_workers=2) as executor:
        for i in range(2):
            executor.submit(db.update, i)

    print(f'ending value is {db.value}')
