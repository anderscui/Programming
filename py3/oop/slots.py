# coding=utf-8


class Pixel:
    __slots__ = ('x', 'y')


class OpenPixel(Pixel):
    pass


class ColorPixel(Pixel):
    # (x, y, color), no __dict__
    __slots__ = ('color',)


if __name__ == '__main__':
    p = Pixel()
    # print(p.__dict__) -> AttributeError:
    p.x, p.y = 10, 10  # OK
    # p.color = 100 -> AttributeError:

    op = OpenPixel()
    print(op.__dict__)  # {}
    op.x = 5
    print(op.__dict__)  # {}
    print(op.x)  # 5

    op.color = 'green'  # -> __dict__
    print(op.__dict__)  # {'color': 'green'}

    print(type(op).__name__)
