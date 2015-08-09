def count_down(start):
    n = start

    def display():
        print('T-minus %d' % n)

    while n > 0:
        display()
        n -= 1


count_down(5)


##

def countdown(start):
    n = start

    def display():
        print('T-minus %d' % n)

    def decrement():
        nonlocal
        n -= 1

    while n > 0:
        display()
        decrement()
