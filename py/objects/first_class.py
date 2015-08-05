# All objects in Python are said to be "first class".
#   All objects that can be named by an id have equal status
#   All objects that can be named by an id can be treated as data

items = {
    'number': 42,
    'text': 'hello world'
}

items['func'] = abs  # add a func

import math
items['mod'] = math  # add a module

items['error'] = ValueError  # add a error type


## everything is first-class: compact & flexible
line = 'GOOG,100,490.10'
field_types = [str, int, float]
raw_fields = line.split(',')
fields = [ty(val) for ty, val in zip(field_types, raw_fields)]
print(fields)