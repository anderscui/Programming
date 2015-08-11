class TypeProperty(object):

    def __init__(self, name, type, default=None):
        self.name = '_' + name
        self.type = type

        self.default = default if default else type()

    def __get__(self, instance, owner):
        return getattr(instance, self.name, self.default)

    def __set__(self, instance, value):
        if not isinstance(value, self.type):
            raise TypeError('Must be a %s' % self.type)
        setattr(instance, self.name, value)

    def __delete__(self, instance):
        raise AttributeError('Cannot delete attribute')


class Foo(object):
    name = TypeProperty("name", str)
    num = TypeProperty("num", int, 42)


f = Foo()
a = f.name
f.name = "Guido"
del f.name