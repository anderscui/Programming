# coding=utf-8
import sys


class LookingGlass:
    def __enter__(self):
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'JABBERWOCKY'

    def reverse_write(self, text):
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('Please DO NOT divide by zero.')
            return True


if __name__ == '__main__':
    print(type(LookingGlass()))

    # context manager is the object
    # the returned value is bound to what
    with LookingGlass() as what:
        print('Alice')
        print(f'what: {what}')

    # after exit, the `write` is back to normal.
    print('Back to normal:')
    print(f'what: {what}')
