def countdown(n):
    local = [n]

    def next():
        # nonlocal n
        r = local[0]
        local[0] -= 1
        return r

    return next


next = countdown(5)
while True:
    v = next()
    print v
    if not v: break

## class version
class Countdown(object):
    def __init__(self, n):
        self.n = n

    def next(self):
        r = self.n
        self.n -= 1
        return r

c = Countdown(5)
while True:
    v = c.next()
    print v
    if not v: break
    