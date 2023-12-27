# coding=utf-8
from pydantic import BaseModel


class Foo(BaseModel):
    count: int
    size: float | None = None


class Bar(BaseModel):
    apple: str = 'x'
    banana: str = 'y'


class Spam(BaseModel):
    foo: Foo
    bars: list[Bar]


if __name__ == '__main__':
    m = Spam(foo={'count': 3},
             bars=[{'apple': 'x1'}, {'apple': 'x2'}])
    print(m)
    print(m.model_dump(exclude_defaults=True))
