def receiver():
    print('Ready to receive')
    while True:
        n = (yield)
        print('Got %s' % n)

r = receiver()
r.next()  # advance to first yield
r.send(1)
r.send(2)
r.send('hello')