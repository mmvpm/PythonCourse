"""Entry point to the application."""

import argparse
import types

from myawesomescript.cowsay import wrap_with_cow
from myawesomescript.highlight import highlight_code
from myawesomescript.time import get_current_time

# All actions and their implementations
ACTIONS = types.MappingProxyType({
    'highlight': highlight_code,
    'cowsay': wrap_with_cow,
    'time': get_current_time,
})


def main():
    """Entry point."""
    parser = argparse.ArgumentParser('my-awesome-script')

    parser.add_argument(
        'action',
        type=str,
        help=' | '.join(ACTIONS.keys()),
    )
    parser.add_argument(
        'data',
        type=str,
        help='text data for action',
    )

    args = parser.parse_args()
    print(ACTIONS[args.action](args.data))
