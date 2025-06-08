# coding=utf-8
import typer
from rich import print
from rich.table import Table
from rich.console import Console

console = Console()
err_console = Console(stderr=True)

data = {
    "name": "Rick",
    "age": 42,
    "items": [{"name": "Portal Gun"}, {"name": "Plumbus"}],
    "active": True,
    "affiliation": None,
}

def main(good: bool=True):
    print('[bold green]Usage[/bold green]')
    print('Here is the data')
    print(data)

    table = Table("Name", "Item")
    table.add_row("Rick", "Portal Gun")
    table.add_row("Morty", "Plumbus")
    console.print(table)
    err_console.print('some simple bugs.')

    # colors
    if good:
        msg = typer.style('good', fg=typer.colors.GREEN, bold=True)
    else:
        msg = typer.style('not so good', fg=typer.colors.BLUE)
    typer.echo(msg)


if __name__ == '__main__':
    typer.run(main)
