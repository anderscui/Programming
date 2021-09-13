import time
import threading


def myfunc(name):
    print(f'myfunc started with {name}')
    time.sleep(3)
    print('myfunc ended')


if __name__ == '__main__':
    print('main started')
    t = threading.Thread(target=myfunc, args=['py'])
    t.start()
    print('main ended')
