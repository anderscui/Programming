a = 42
b = 13.142783
c = 'hello'
d = {'x': 13, 'y': 1.54321, 'z': 'world'}
e = 5628398123741234

print('a is %d' % a)
print('%10d %f' % (a, b))
print('%+010d %E' % (a, b))
print('%(x)-10d %(y)0.3g' % d)
print('%0.4s %s' % (c, d['z']))
print('%*.*f' % (5, 3, b))
print('e = %d' % e)

s = 'Your name is {0} and your age is {age}'
print(s.format('anders', age=34))

# ####

print("{0} {1} {2}".format('GOOG', 100, 490.10))
print("{name} {shares} {price}".format(name='GOOG', shares=100, price=490.10))
print("Hello {0}, your age is {age}".format("Elwood", age=47))
print("Use {{ and }} to output single curly braces".format())


# ####
name = "Guido"
r = '{0!r:^20}'.format(name)  # r = " 'Guido' "
