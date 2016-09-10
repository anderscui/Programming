import logging
from contextlib import contextmanager


def my_func():
    logging.debug('Some debug data')
    logging.error('Error log data')
    logging.debug('More debug data')


@contextmanager
def debug_logging(level):
    logger = logging.getLogger()
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield
    finally:
        logger.setLevel(old_level)

with debug_logging(logging.DEBUG):
    print('Inside: ')
    my_func()

print('After: ')
my_func()
