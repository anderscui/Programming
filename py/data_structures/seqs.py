
l = [1, 2, 3, 4, 5]
print(l)
del l[1:3]
print(l)

cities = ['Paris', 'Shanghai', 'London']
cities2 = list(cities)
cities2.sort()
print(cities2)
cities2 = list(cities)
cities2.sort(key=lambda c: c[-1])
print(cities2)