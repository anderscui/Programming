# coding=utf-8
from typing import Literal


def transform(data: str, mode: Literal["split", "upper"]) -> list[str] | str:
    if mode == "split":
        return data.split()
    else:
        return data.upper()


if __name__ == '__main__':
    print(transform('hello world', mode='split'))
    print(transform('hello world', mode='upper'))
    print(transform('hello world', mode='lower'))
