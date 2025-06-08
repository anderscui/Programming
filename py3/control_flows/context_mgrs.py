# coding=utf-8
import contextlib


@contextlib.contextmanager
def handle_write_file(path: str):
    try:
        with open(path, 'w') as f:
            f.write('hello, world\n')
            yield f
            f.write('bye, world!\n')
    except Exception as e:
        raise Exception() from e


if __name__ == '__main__':
    fp = 'test.log'
    with handle_write_file(fp) as f:
        f.write('write something now...\n')
    print('file closed:', f.closed)
    print(open(fp).read())
