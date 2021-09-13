import logging
import threading
import time


def thread_func(name):
    logging.info(f'thread {name} - {threading.get_ident()}: starting')
    time.sleep(0.5)
    logging.info(f'thread {name}: finishing')


if __name__ == '__main__':
    fmt = "%(asctime)s: %(message)s"
    logging.basicConfig(format=fmt, level=logging.INFO, datefmt='%H:%M:%S')

    logging.info('main: before creating')
    x = threading.Thread(target=thread_func, args=('second',), daemon=True)
    logging.info('main: before running')
    x.start()
    logging.info('main: wait for finishing')
    x.join()
    logging.info('main: job done')
