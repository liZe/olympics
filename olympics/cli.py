"""CLI internal functions."""

from rich.console import Console
from rich.table import Table

from . import db


def top_countries(top=10, file=None):
    table = Table(title=f"Top {top} countries")

    table.add_column('Country')
    table.add_column('Gold', justify='right')
    table.add_column('Silver', justify='right')
    table.add_column('Bronze', justify='right')
    table.add_column('Total', justify='right')

    for row in db.get_top_countries(top):
        table.add_row(
            row['name'],
            str(row['gold']),
            str(row['silver']),
            str(row['bronze']),
            str(row['gold'] + row['silver'] + row['bronze']),
        )

    console = Console(file=file)
    console.print(table)


def top_collective(top=10, file=None):
    table = Table(title=f'Top {top} collective events')

    table.add_column('Country')
    table.add_column('Medals', justify='right')

    for row in db.get_top_collective(top):
        table.add_row(
            row['country'],
            str(row['medals']),
        )

    console = Console(file=file)
    console.print(table)


def top_individual(top=10, file=None):
    table = Table(title=f'Top {top} individual events')

    table.add_column('Name')
    table.add_column('Gender')
    table.add_column('Country')
    table.add_column('Medals', justify='right')

    for row in db.get_top_individual(top):
        table.add_row(
            row['name'],
            row['gender'].capitalize(),
            row['country'],
            str(row['medals']),
        )

    console = Console(file=file)
    console.print(table)
