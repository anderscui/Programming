# coding=utf-8
import typer
from typing_extensions import Annotated


def main(name: Annotated[str, typer.Argument(help='Name of the user to greet',
                                             metavar='✨username✨',
                                             envvar='USER', show_envvar=False)] = 'random guest'):
    """
    Say hello to the friendly user.
    """
    if name is None:
        print('Hello typer.')
    else:
        print(f'Hello {name}')


if __name__ == '__main__':
    typer.run(main)
