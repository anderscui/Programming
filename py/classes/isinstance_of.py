class Base(object):
    pass


class Derived(Base):
    pass

b = Base()
d = Derived()

print(isinstance(b, Base))
print(isinstance(b, Derived))
print(isinstance(d, Base))
print(isinstance(d, Derived))
