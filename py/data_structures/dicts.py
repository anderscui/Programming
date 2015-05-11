
addresses = {
    'andersc': 'anderscui@gmail.com',
    'larry': 'larry@wall.org',
    'someone': 'someone@yahoo.com',
    'unknown': 'unknown@yahoo.com',
}

print('There are {} addresses.'.format(len(addresses)))
print("andersc's address is {0}".format(addresses['andersc']))

del addresses['unknown']
print('After i delete the unknown one, now i have {} addresses'.format(len(addresses)))

for name in addresses:
    print('name: ' + name)

for name, addr in addresses.items():
    print('name: {}, address: {}'.format(name, addr))

# adding an item
addresses['Guido'] = 'guido@python.org'

# checking
if 'Guido' in addresses:
    print("Guido's address is {}".format(addresses['Guido']))

