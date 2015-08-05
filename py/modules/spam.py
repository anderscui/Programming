a = 10
print('a is %d' % a)


def foo():
    print('I am foo and a is %s' % a)


def bar():
    print('I am bar and I am calling foo')
    foo()


class Spam(object):
    def grok(self):
        print('I am spam.grok')

