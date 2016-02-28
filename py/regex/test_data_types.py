import re

re_numbers = re.compile(r'[-+]?\d*\.\d+|\d+')
re_pure_number = re.compile(r'^[-+]?\d*\.\d+|\d+$')
re_number_with_unit = re.compile(r'^[-+]?(\d*\.\d+|\d+)[a-zA-Z]+')
re_money = re.compile(r'^\$(\d*\.\d+|\d+)$')

re_en_word = re.compile(r"^[a-z-'.&]+$")

def test_re_numbers():
    s = 'numbers: -1.1, 3.2 or 5'
    result = re_numbers.findall(s)
    assert len(result) == 3
    assert result[1] == '3.2'


def isnumeric(s):
    return re_pure_number.match(s) is not None


def ismoney(s):
    return re_money.match(s) is not None


def isnumeric_with_unit(s):
    return re_number_with_unit.match(s) is not None


def is_english_word(w):
    return re_en_word.match(w) is not None


def test_isnumeric():
    assert not isnumeric('')
    assert not isnumeric('abc')
    assert not isnumeric('a123')
    assert not isnumeric('123ab')

    assert isnumeric('-1.1')
    assert isnumeric('.123')
    assert isnumeric('3.14')
    assert isnumeric('17')


def test_ismoney():
    assert not ismoney('')
    assert not ismoney('123')

    assert ismoney('$123')
    assert ismoney('$.123')
    assert ismoney('$6.123')


def test_isnumeric_with_unit_with_unit():
    assert not isnumeric_with_unit('')
    assert not isnumeric_with_unit('abc')
    assert not isnumeric_with_unit('a123')

    assert not isnumeric_with_unit('-1.1')
    assert not isnumeric_with_unit('.123')
    assert not isnumeric_with_unit('3.14')
    assert not isnumeric_with_unit('17')

    assert isnumeric_with_unit('123C')
    assert isnumeric_with_unit('12.5cm')
    assert isnumeric_with_unit('-12.5cm')

    assert isnumeric_with_unit('1000cm3')


def test_is_english_word():
    assert not is_english_word('10')
    assert not is_english_word('p0ssword')
    assert not is_english_word('p@ssword')
    assert not is_english_word('is_good')
    assert not is_english_word(r'at\a')
    assert not is_english_word('Good')

    assert is_english_word('a')
    assert is_english_word('word')
    assert is_english_word('first-class')
    assert is_english_word("don't")
    assert is_english_word('u.s.a.')
    assert is_english_word('at&t')


