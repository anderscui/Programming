# coding=utf-8
import itertools
import time
from threading import Thread, Event

spin_chars = r'\|/-'
# spin_chars = r'1234567890'


def spin(msg: str, done: Event):
    status = ''
    for c in itertools.cycle(spin_chars):
        status = f'\r{c} {msg}'
        print(status, end='', flush=True)
        if done.wait(.2):
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')


def slow():
    # sleep: blocks the calling thread, but releases the GIL, allow other threads to run.
    time.sleep(3)
    return 42


def supervisor() -> int:
    done = Event()
    spinner = Thread(target=spin, args=('thinking!', done))
    print(f'spinner object: {spinner}')
    spinner.start()
    result = slow()
    done.set()
    # wait until the spinner thread finishes
    spinner.join()
    return result


def main():
    result = supervisor()
    print(f'Answer: {result}')


if __name__ == '__main__':
    main()
