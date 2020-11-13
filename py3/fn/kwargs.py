# coding=utf-8


def log(msg, *values):
    # values is a tuple
    if values:
        val_str = ', '.join(str(v) for v in values)
        print(f'{msg}: {val_str}')
    else:
        print(msg)


if __name__ == '__main__':
    log('My numbers are', 1, 2)
    log('Hi there')

    # pass list as args
    colors = [1, 2, 3]
    log('Favorite colors', *colors)
