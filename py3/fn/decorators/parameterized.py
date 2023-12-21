# coding=utf-8
registry = set()


def register(active=True):
    def decorate(func):
        print(f'running register (active={active}) -> decorate({func})')
        if active:
            registry.add(func)
        else:
            registry.discard(func)
        return func
    return decorate


@register(active=False)
def f1():
    print('running f1()')


@register()
def f2():
    print('running f2()')


@register
def f3():
    print(f'running f3()')


if __name__ == '__main__':
    f1()
    f2()
    f3()
