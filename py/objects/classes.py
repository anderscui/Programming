class Foo(object):

    def bar(self, x):
        print(x)


print(type(Foo))
print(Foo.__doc__)
print(Foo.__name__)
print(Foo.__bases__)
print(Foo.__dict__)
print(Foo.__module__)
# print(Foo.__abstractmethods__)
print(type(Foo()))