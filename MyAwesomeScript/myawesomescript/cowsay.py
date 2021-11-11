"""Cowsay action implementation."""

from cowpy import cow


def wrap_with_cow(message: str) -> str:
    """Wrap message.

    Args:
        message: message to say

    Returns:
        message with cow
    """
    my_cow = cow.Moose()
    return my_cow.milk(message)
