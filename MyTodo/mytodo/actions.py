"""Actions."""

from typing import final

from mytodo.model import Task
from mytodo.storage import Storage


class BaseAction(object):
    """Base class for actions."""

    def __init__(self, params: list[str]):
        """Initialize action."""
        raise NotImplementedError()

    def apply_to(self, storage: Storage):
        """Apply action to storage."""
        raise NotImplementedError()


@final
class ActionAdd(BaseAction):
    """Action: add 'title' 'description'."""

    def __init__(self, params: list[str]):
        """Initialize add action."""
        if len(params) != 2:
            raise ValueError('"add" action expects exactly 2 params')

        title, description = params
        self.task = Task(title, description)

    def apply_to(self, storage: Storage):
        """Add task to storage."""
        storage.add(self.task)


@final
class ActionShow(BaseAction):
    """Action: show <int>."""

    def __init__(self, params: list[str]):
        """Initialize show action."""
        if len(params) != 1:
            raise ValueError('"show" action expects exactly 1 param')

        self.task_count = int(params[0])

    def apply_to(self, storage: Storage):
        """Show last tasks in storage."""
        tasks = storage.show(self.task_count)
        for task in tasks:
            print(task)


@final
class ActionDone(BaseAction):
    """Action: done <int>."""

    def __init__(self, params: list[str]):
        """Initialize done action."""
        if len(params) != 1:
            raise ValueError('"done" action expects exactly 1 param')

        self.task_index = int(params[0])

    def apply_to(self, storage: Storage):
        """Remove task from storage."""
        storage.done(self.task_index)


@final
class ActionFind(BaseAction):
    """Action: find 'text'."""

    def __init__(self, params: list[str]):
        """Initialize find action."""
        if len(params) != 1:
            raise ValueError('"find" action expects exactly 1 param')

        self.text = params[0]

    def apply_to(self, storage: Storage):
        """Find in storage."""
        task_opt = storage.find(self.text)
        if task_opt is not None:
            print(task_opt)
        else:
            print('Task not found')
