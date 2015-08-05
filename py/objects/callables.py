def foo(x, y=1):
    """foo func"""
    i = 1
    j = 0
    return x + y

# custom function
print(foo.__doc__)
print(foo.__name__)
print(foo.__dict__)
print(foo.__code__)
print(foo.__defaults__)
print(foo.__globals__)
print(foo.__closure__)

print('lambda exp')
bar = lambda x, y: x + y
print(bar.__doc__)
print(bar.__name__)
print(bar.__dict__)
print(bar.__code__)
print(bar.__defaults__)
print(bar.__globals__)
print(bar.__closure__)


print('methods')


class Foo(object):
    def inst_method(self, arg):
        """inst method"""
        print(arg)

    @classmethod
    def cls_method(cls, arg):
        print(arg)

    @staticmethod
    def static_method(arg):
        print(arg)

f = Foo()
print(type(f.inst_method))
print(type(Foo.inst_method))
print(type(Foo.cls_method))
print(type(Foo.static_method))

print(f.inst_method.__doc__)
print(f.inst_method.__name__)
print(f.inst_method.__class__)
print(f.inst_method.__func__)
print(f.inst_method.__self__)


print('built-in funcs and methods')
bf = max
print(bf.__doc__)
print(bf.__name__)
print(bf.__self__)
