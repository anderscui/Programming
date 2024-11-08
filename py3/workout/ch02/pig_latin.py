# coding=utf-8


def pig_latin(s: str):
    if not s:
        return s
    first_upper = s[0].isupper()
    if s[0].lower() in 'aeiou':
        converted = f'{s}way'
    else:
        converted = f'{s[1:]}{s[0]}ay'
    if first_upper:
        converted = converted.capitalize()
    return converted


if __name__ == '__main__':
    assert pig_latin('air') == 'airway'
    assert pig_latin('Air') == 'Airway'
    assert pig_latin('python') == 'ythonpay'
    assert pig_latin('Python') == 'Ythonpay'

    # TODO: punctuations
    print(pig_latin('test.'))
    print(pig_latin('Test.'))
