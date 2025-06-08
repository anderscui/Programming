# coding=utf-8
import typer
from typing_extensions import Annotated


def main(
        name: str,
        lastname: Annotated[str, typer.Option('--name',
                                              '-n',
                                              help='Last name of user',
                                              prompt=True)],
        formal: Annotated[bool, typer.Option('--formal', '-f')] = False
):
    """
    Say hi to NAME, optionally with a --lastname.

    example: python options_short.py anders -fn cui
    """
    if formal:
        print(f'Good day Ms. {name} {lastname}.')
    else:
        print(f'Hello {name} {lastname}')


if __name__ == '__main__':
    typer.run(main)
