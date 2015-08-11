class A(object):
    def __init__(self):
        self.__X = 3

    def __spam(self):
        pass

    def bar(self):
        self.__spam()


class B(A):
    def __init__(self):
        A.__init__(self)
        self.__X = 37

    def __spam(self):
        pass

a = A()
print(a._A__X)
print(a.__X)