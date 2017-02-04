# coding=utf-8
from __future__ import unicode_literals


def psychologist():
    print('Please tell me your problems')
    while True:
        answer = (yield)
        if answer:
            if answer.endswith('?'):
                print('do not ask yourself too many questions')
            elif 'good' in answer:
                print('good, go on')
            elif 'bad' in answer:
                print('do not be so negative')


if __name__ == '__main__':
    free = psychologist()
    next(free)

    free.send('I feel bad')
    free.send('Why i should not?')
    free.send('very good of you')
