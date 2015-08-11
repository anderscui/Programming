def line_splitter(delimiter=None):
    print('Ready to split')
    result = None
    while True:
        line = (yield result)
        result = line.split(delimiter)

r = line_splitter(",")
print(r.next())  # advance to first yield
print(r.send('a,b,c'))
print(r.send('1,2,3'))