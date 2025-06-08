# coding=utf-8
import typer


def main(name: str, lastname: str='', formal: bool=False):
    """
    This docstring will be used in the help text.

    # `default` value convert argument to option

    # usage: python first.py anders --lastname cui --formal

    :param name:
    :param lastname:
    :param formal:
    """
    if formal:
        print(f'Good day Ms. {name.capitalize()} {lastname.capitalize()}.')
    else:
        print(f'Hello {name} {lastname}')


if __name__ == '__main__':
    typer.run(main)
