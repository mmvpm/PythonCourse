def test_class_exists():
    from todo.models import ToReadItem

    assert isinstance(ToReadItem, type)


def test_there_are_attributes():
    from todo.models import ToReadItem

    heading = 'test'
    url = 'http://ya.ru'
    item = ToReadItem(heading, url)

    assert item.heading == heading
    assert item.url == url
    assert item.done is False


def test_fabric_method(monkeypatch):
    from todo.models import ToReadItem

    value = 'some input'

    monkeypatch.setitem(__builtins__, 'input', lambda _: value)
    item = ToReadItem.construct()

    assert item.heading == value
    assert item.url == value
    assert item.done is False


def test_representation():
    from todo.models import ToReadItem

    heading = 'test'
    url = 'http://ya.ru'
    item = ToReadItem(heading, url)

    assert str(item) == '- ToRead: {} {}'.format(heading, url)

    item.done = True

    assert str(item) == '+ ToRead: {} {}'.format(heading, url)
