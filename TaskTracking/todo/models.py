class BaseItem(object):
    def __init__(self, heading, done = False):
        self.heading = heading
        self.done = done

    def __repr__(self):
        return self.__class__.__name__

    @classmethod
    def construct(cls):
        raise NotImplementedError()


class ToDoItem(BaseItem):
    action = 'ToDo'

    def __str__(self):
        done_mark = '+' if self.done else '-'
        return f'{done_mark} {self.action}: {self.heading}'

    @classmethod
    def construct(cls):
        heading = input('Input heading: ')
        return cls(heading)


class ToBuyItem(BaseItem):
    action = 'ToBuy'
    
    def __init__(self, heading, price):
        super().__init__(heading)
        self.price = price

    def __str__(self):
        done_mark = '+' if self.done else '-'
        return f'{done_mark} {self.action}: {self.heading} for {self.price}'

    @classmethod
    def construct(cls):
        heading = input('Input heading: ')
        price = input('Input price: ')
        return cls(heading, price)


class ToReadItem(BaseItem):
    action = 'ToRead'

    def __init__(self, heading, url):
        super().__init__(heading)
        self.url = url

    def __str__(self):
        done_mark = '+' if self.done else '-'
        return f'{done_mark} {self.action}: {self.heading} {self.url}'
    
    @classmethod
    def construct(cls):
        heading = input('Input heading: ')
        url = input('Input url: ')
        return cls(heading, url)
