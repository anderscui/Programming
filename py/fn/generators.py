def countdown(n):
    print('Counting down from %d' % n)
    while n > 0:
        yield n
        n -= 1
    return

c = countdown(5)
print(c.next())
for n in c:
    print(n)

c.close()
c.next()