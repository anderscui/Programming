# coding=utf-8


def tag(name, *content, class_=None, **attrs):
    """Generate one or more HTML tags"""
    if class_ is not None:
        attrs['class'] = class_
    attr_pairs = (f' {attr}="{val}"' for attr, val in sorted(attrs.items()))
    attr_str = ''.join(attr_pairs)
    if content:
        elems = (f'<{name}{attr_str}>{elem}</{name}' for elem in content)
        return '\n'.join(elems)
    return f'<{name}{attr_str} />'


def f(a, *, b):
    # keyword-only argument `b`
    return a, b


def divmod(a, b, /):
    # positional-only arguments
    return a // b, a % b


if __name__ == '__main__':
    print(tag('br'))
    print(tag('p', 'hello'))
    print(tag('p', 'hello', id=33))
    print(tag('p', 'hello', 'world', class_='sidebar'))
    contents = ['hello', 'world', '!']
    print(tag('p', *contents, class_='sidebar'))
    # all kw
    print(tag(content='testing', name='img'))
    # all kw
    args = {
        'name': 'img',
        'title': 'Sunset Boulevard',
        'src': 'sunset.jpg',
        'class': 'framed'
    }
    print(tag(**args))

    # f
    # TypeError: f() takes 1 positional argument but 2 were given
    # print(f(1, 2))
    # print(f(1))
    print(f(1, b=2))
    print(f(a=1, b=2))

    print(divmod(5, 2))
