# coding=utf-8

import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence
        self.words = RE_WORD.findall(sentence)

    def __iter__(self):
        for word in self.words:
            yield word

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return f'Sentence({reprlib.repr(self.sentence)})'


if __name__ == '__main__':
    sent = Sentence('"The time has come," the Walrus said,')
    print(sent)

    for word in sent:
        print(word)

    print(list(sent))
