import re

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'


def test_basic_match():
    assert re.match(r'\d+/\d+/\d+', text1)
    assert not re.match(r'\d+/\d+/\d+', text2)


def test_match_other_than_start():
    assert not re.match(r'\d+/\d+/\d+', 'some' + text1 + 'others')


def test_compile_match():
    re_date = re.compile(r'\d+/\d+/\d+')
    assert re_date.match(text1)
    assert not re_date.match(text2)


def test_search():
    s = 'I am working on 11/06/2012 and 05/18/2016'
    m = re.search(r'\d+/\d+/\d+', s)
    print(m.group(0))
    print(s[m.start(): m.end()])


def test_findall():
    t = 'Today is 11/27/2012. PyCon starts 2/14/2016'
    re_date = re.compile(r'\d+/\d+/\d+')

    m = re_date.findall(t)
    assert len(m) == 2
    assert m[0] == '11/27/2012'
    assert m[1] == '2/14/2016'


def test_match_groups():
    re_date = re.compile(r'(\d+)/(\d+)/(\d+)')
    m = re_date.match('03/27/2012')
    assert len(m.groups()) == 3
    assert m.group(1) == '03'
    assert m.group(2) == '27'
    assert m.group(3) == '2012'
    assert m.group(0) == '03/27/2012'


def test_find_all_groups():
    re_date = re.compile(r'(\d+)/(\d+)/(\d+)')
    m = re_date.findall('03/27/2012, 11/06/2000')
    assert len(m) == 2
    for m, d, y in m:
        print('{}-{}-{}'.format(y, m, d))


def test_finditer():
    re_date = re.compile(r'(\d+)/(\d+)/(\d+)')
    for m in re_date.finditer('03/27/2012, 11/06/2000'):
        # print(type(m.groups())) # tuple of str
        print(m.groups())


re_data_line = re.compile(r'\t')
def test_csv():
    parts = re_data_line.split('a b\t1900\t1\t2\t3')
    print(parts)
