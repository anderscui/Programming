class LazyDB(object):
    def __init__(self):
        self.exists = 5

    def __getattr__(self, name):
        value = 'Value for %s' % name
        setattr(self, name, value)
        return value

data = LazyDB()
print('Before: ', data.__dict__)
print('foo', data.foo)
print('After: ', data.__dict__)

##

class ValidatingDB(object):
    def __init__(self):
        self.exists = 5

    def __getattribute__(self, name):
        print('Called __getattribute__(%s)' % name)
        try:
            return super().__getattribute__(name)
        except AttributeError:
            value = 'Value for %s' % name
            setattr(self, name, value)
            print('Added (%s) attr' % name)
            return value

data = ValidatingDB()
print('exists: ', data.exists)
print('foo: ', data.foo)
print('foo: ', data.foo)
