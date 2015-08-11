a = [1, 2, 3, 4, 5]
b = (i*10 for i in a)
print(b)
print(b.next())
print(b.next())
b.close()