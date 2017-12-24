# coding=utf-8


class DuplicateValueError(ValueError):
    """Raised when duplicate value is added to a distinct dict"""


class distinctdict(dict):
    def __setitem__(self, key, value):
        if value in self.values():
            if (key in self and self[key] != value) or (key not in self):
                raise DuplicateValueError('This value already exists for a diff key.')

        super().__setitem__(key, value)


if __name__ == '__main__':
    dd = distinctdict()
    dd['key'] = 'value'
    dd['key2'] = 'value'

