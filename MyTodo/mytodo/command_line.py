"""Entry point module."""

import sys
import types

from mytodo.actions import (ActionAdd, ActionDone, ActionFind, ActionShow,
                            BaseAction)
from mytodo.storage import Storage

# Actions with todo list
ACTIONS = types.MappingProxyType({
    'add': ActionAdd,
    'show': ActionShow,
    'done': ActionDone,
    'find': ActionFind,
})


def read_action() -> BaseAction:
    """Parse console arguments."""
    argv = sys.argv
    if len(argv) < 2:
        raise ValueError('Script expects at least 1 params')

    _, action, *action_params = argv
    if action not in ACTIONS:
        raise ValueError('Unknown action')

    action_type = ACTIONS[action]
    return action_type(action_params)


def main() -> None:
    """Entry point function."""
    action = read_action()
    storage = Storage('todo.json')
    action.apply_to(storage)
