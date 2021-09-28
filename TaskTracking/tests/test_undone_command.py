def test_class_exists():
    from todo.commands import UndoneCommand

    assert isinstance(UndoneCommand, type)


def test_command_label_in_list():
    from todo.commands import UndoneCommand
    from todo.runtime import get_routes

    assert UndoneCommand().label in get_routes()


def test_command_execution(monkeypatch):
    from todo.commands import UndoneCommand
    from todo.runtime import perform_command
    from todo.models import ToDoItem
    from todo.storage import Storage

    monkeypatch.setitem(__builtins__, 'input', lambda _: 0)

    item = ToDoItem('test')
    item.done = True

    s = Storage()
    s.items.clear()
    s.items.append(item)

    perform_command(UndoneCommand().label)

    assert item.done is False
