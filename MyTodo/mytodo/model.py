"""Models."""


class Task(object):
    """Task(title, description)."""

    def __init__(self, title: str, description: str):
        """Initialize the task."""
        self.title = title
        self.description = description

    def __str__(self) -> str:
        """Convert task to string."""
        return 'Task({0}: {1})'.format(
            self.title,
            self.description,
        )

    def __repr__(self) -> str:
        """Convert task to string repr."""
        return str(self)
