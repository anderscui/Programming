# coding=utf-8
import re
import reprlib
from collections.abc import Iterable, Iterator

RE_WORD = re.compile(r'\w+')


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, i):
        return self.words[i]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return f'Sentence({reprlib.repr(self.text)})'


class Sentence2:
    """A classic Iterator"""
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return f'Sentence({reprlib.repr(self.text)})'

    def __iter__(self):
        return SentenceIterator(self.words)


class SentenceIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word

    def __iter__(self):
        return self


class Sentence3:
    """An idiomatic version"""
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return f'Sentence({reprlib.repr(self.text)})'

    def __iter__(self):
        for word in self.words:
            # print('in', word)
            yield word


class Sentence4:
    """An lazy version"""
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return f'Sentence({reprlib.repr(self.text)})'

    def __iter__(self):
        for m in RE_WORD.finditer(self.text):
            yield m.group()


class Sentence5:
    """An gen exp version"""
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return f'Sentence({reprlib.repr(self.text)})'

    def __iter__(self):
        return (m.group() for m in RE_WORD.finditer(self.text))


if __name__ == '__main__':
    # when Python needs to iterate, it calls iter(x)
    # * __iter__
    # * __getitem__ (from 0)
    # * TypeError
    sent = Sentence('I like Python programming lang.')
    print(repr(sent))
    for w in sent:
        print(w, end=' ')
    print()
    print(list(sent))

    assert not issubclass(Sentence, Iterable)
    assert issubclass(Sentence2, Iterable)
    assert issubclass(Sentence3, Iterable)

    sent = Sentence3('I like Python programming lang.')
    print(list(sent))
    it = iter(sent)
    # a `generator` is an `Iterator`
    assert isinstance(it, Iterator)
    print(type(it), list(it))
    it = iter(sent)
    for item in it:
        print(item)

    sent = Sentence4('I like Python programming lang.')
    print(list(sent))

    sent = Sentence5('I like Python programming lang.')
    it = iter(sent)
    print(type(it), list(it))
