"""Storage implementation."""

import json
from os import path
from typing import Optional, final

from mytodo.model import Task


@final
class Storage(object):
    """Json-file storage."""

    def __init__(self, filename: str) -> None:
        """Initialize object."""
        self.filename = filename
        self.tasks: list[Task] = []
        if path.exists(filename):
            self.tasks = self._read_json()

    def add(self, task: Task) -> None:
        """Add task to the list."""
        self.tasks.append(task)
        self._write_json()

    def show(self, task_count: int) -> list[Task]:
        """Show last `task_count` tasks."""
        start_index = max(0, len(self.tasks) - task_count)
        last_tasks = self.tasks[start_index:]
        return last_tasks[::-1]

    def done(self, task_index: int) -> None:
        """Remove task with index `task_index`."""
        self.tasks.pop(task_index)
        self._write_json()

    def find(self, text: str) -> Optional[Task]:
        """Find task which contains `text`."""
        for task in self.tasks:
            if text in task.title or text in task.description:
                return task
        return None

    def _read_json(self) -> list[Task]:
        with open(self.filename, 'rt') as json_file:
            return [
                Task(*task.values())
                for task in json.load(json_file)
            ]

    def _write_json(self) -> None:
        with open(self.filename, 'wt') as json_file:
            tasks_json = [
                {
                    'title': task.title,
                    'description': task.description,
                }
                for task in self.tasks
            ]
            json.dump(tasks_json, json_file)
