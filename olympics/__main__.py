"""CLI public options."""

import argparse
from . import cli

parser = argparse.ArgumentParser(
    prog='olympics',
    description='Display various information about Olympics results',
)
parser.add_argument(
    'command',
    help='command to launch',
    choices=('countries', 'collective', 'individual','search'),
)
parser.add_argument(
    '--top',
    help='number of top elements to display',
    type=int,
    default=10,
)

parser.add_argument(
    '--query',
    help='Search query for countries (required for search command)',
    required=False,
    type=float,
    default=10,
)

def main(argv=None):
    args = parser.parse_args(argv)
    if (top := int(args.top)) <= 0:
        raise argparse.ArgumentTypeError(f'{top} is not a positive number')
    match args.command:
        case 'countries':
            cli.top_countries(top)
        case 'collective':
            cli.top_collective(top)
        case 'individual':
            cli.top_individual(top)
        case 'search':
            if not args.query:
                raise argparse.ArgumentTypeError('query is required for search command')
            cli.search_countries(args.query)


if __name__ == '__main__':  # pragma: no cover
    main()
