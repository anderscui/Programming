# coding=utf-8
import random

import typer
from typing_extensions import Annotated


def get_name():
    return random.choice(['Python', 'R', 'Rust'])


def main(name: Annotated[str, typer.Argument(default_factory=get_name)]):
    if name is None:
        print('Hello typer.')
    else:
        print(f'Hello {name}')


if __name__ == '__main__':
    typer.run(main)
