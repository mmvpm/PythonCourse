def test_class_exists():
    from todo.commands import DoneCommand

    assert isinstance(DoneCommand, type)


def test_command_label_in_list():
    from todo.commands import DoneCommand
    from todo.runtime import get_routes

    assert DoneCommand().label in get_routes()


def test_command_execution(monkeypatch):
    from todo.commands import DoneCommand
    from todo.runtime import perform_command
    from todo.models import ToDoItem
    from todo.storage import Storage

    monkeypatch.setitem(__builtins__, 'input', lambda _: 0)

    item = ToDoItem('test')
    item.done = False

    s = Storage()
    s.items.clear()
    s.items.append(item)

    perform_command(DoneCommand().label)

    assert item.done is True
