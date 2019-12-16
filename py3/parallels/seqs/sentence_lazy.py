# coding=utf-8

import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence

    # def __iter__(self):
    #     for match in RE_WORD.finditer(self.sentence):
    #         yield match.group()

    def __iter__(self):
        return (match.group() for match in RE_WORD.finditer(self.sentence))

    def __repr__(self):
        return f'Sentence({reprlib.repr(self.sentence)})'


if __name__ == '__main__':
    sent = Sentence('"The time has come," the Walrus said,')
    print(sent)

    for word in sent:
        print(word)

    print(list(sent))
