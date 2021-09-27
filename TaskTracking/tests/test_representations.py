def test_to_buy_item():
    from todo.models import ToBuyItem

    item = ToBuyItem('header', 'price')
    assert str(item).startswith('- ToBuy: ')

    item.done = True
    assert str(item).startswith('+ ToBuy: ')


def test_to_do_item():
    from todo.models import ToDoItem

    item = ToDoItem('subject')
    assert str(item).startswith('- ToDo: ')

    item.done = True
    assert str(item).startswith('+ ToDo: ')
