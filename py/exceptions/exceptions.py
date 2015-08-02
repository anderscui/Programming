try:
    f = open('foo.txt')
except IOError as e:
    print(e)
