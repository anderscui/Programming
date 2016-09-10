class FrequencyList(list):
    def __init__(self, members):
        super().__init__(members)

    def frequency(self):
        counts = {}
        for item in self:
            counts.setdefault(item, 0)
            counts[item] += 1
        return counts


if __name__ == '__main__':
    foo = FrequencyList(['a', 'b', 'a', 'c', 'b', 'a', 'd'])
    print('Length is ', len(foo))
    foo.pop()
    print('After pop: ', repr(foo))
    print('Frequency: ', foo.frequency())
