# TODO: Py3?
from collections.abc import Sequence


class BadType(Sequence):
    pass

foo = BadType()
# TypeError: Can't instantiate abstract class BadType with abstract methods __getitem__, __len__
