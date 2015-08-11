enable_tracing = True


def trace(func):
    if enable_tracing:
        def callf(*args, **kwargs):
            print('calling %s: %s, %s' % (func.__name__, args, kwargs))
            r = func(*args, **kwargs)
            print('%s returned: %s' % (func.__name__, r))

            return r

        return callf
    else:
        return func


@trace
def square(x):
    return x * x

val = square(3)