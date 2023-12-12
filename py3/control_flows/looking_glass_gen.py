# coding=utf-8
import contextlib
import sys


@contextlib.contextmanager
def looking_glass():
    def reverse_write(text):
        original_write(text[::-1])

    original_write = sys.stdout.write
    sys.stdout.write = reverse_write
    msg = ''
    try:
        yield 'JABBERWOCKY'
    except ZeroDivisionError:
        msg = 'Please do not divide by zero.'
    finally:
        sys.stdout.write = original_write
        if msg:
            print(msg)


if __name__ == '__main__':
    print(type(looking_glass()))

    # context manager is the object
    # the returned value is bound to what
    with looking_glass() as what:
        print('Alice')
        print(f'what: {what}')

    # after exit, the `write` is back to normal.
    print('Back to normal:')
    print(f'what: {what}')
