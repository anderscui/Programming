# coding=utf-8


def cls_name(obj_or_cls):
    cls = type(obj_or_cls)
    if cls is type:
        cls = obj_or_cls
    return cls.__name__.split('.')[-1]


def display(obj):
    cls = type(obj)
    if cls is type:
        return f'<class {obj.__name__}>'
    elif cls in [type(None), int]:
        return repr(obj)
    else:
        return f'<{cls_name(obj)} object>'


def print_args(name, *args):
    pseudo_args = ', '.join(display(x) for x in args)
    print(f'-> {cls_name(args[0])}.__{name}__({pseudo_args})')


class Overriding:  # <1>
    """a.k.a. data descriptor or enforced descriptor"""

    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)  # <2>

    def __set__(self, instance, value):
        print_args('set', self, instance, value)


class OverridingNoGet:  # <3>
    """an overriding descriptor without ``__get__``"""

    def __set__(self, instance, value):
        print_args('set', self, instance, value)


class NonOverriding:  # <4>
    """a.k.a. non-data or shadowable descriptor"""

    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)


class Managed:  # <5>
    over = Overriding()
    over_no_get = OverridingNoGet()
    non_over = NonOverriding()

    def spam(self):  # <6>
        print(f'-> Managed.spam({display(self)})')


def f():
    return 1


if __name__ == '__main__':
    obj = Managed()

    print('# overriding property')
    _ = obj.over
    # for class prop, no instance
    _ = Managed.over

    obj.over = 1
    # get from instance
    _ = obj.over

    obj.__dict__['over'] = 2
    print(vars(obj))
    # still use descriptor
    _ = obj.over
    print()

    # overriding without __get__
    print('# overriding property without get')
    print(obj.over_no_get)
    print(Managed.over_no_get)

    obj.over_no_get = 1
    print(obj.over_no_get)
    obj.__dict__['over_no_get'] = 2
    print(obj.over_no_get)
    obj.over_no_get = 3
    print(obj.over_no_get)
    print()

    print('# non-overriding property')
    _ = obj.non_over
    obj.non_over = 1
    print(obj.non_over)
    _ = Managed.non_over
    del obj.non_over
    _ = obj.non_over
    print()

    print('overriding a descriptor in the `class`')
    obj = Managed()
    Managed.over, Managed.over_no_get, Managed.non_over = 1, 2, 3
    print(Managed.over, Managed.over_no_get, Managed.non_over)
    print()

    print('bound method')
    obj = Managed()
    print(obj.spam)
    print(Managed.spam)
    obj.spam = 1
    print(obj.spam)
    print()

    print('user defined function')
    # print(dir(f))
