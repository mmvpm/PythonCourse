# ~ collections.defaultdict
class MyDefaultDict(dict):
    
    def __init__(self, default_value):
        super().__init__()
        self.default_value = default_value

    def __repr__(self):
        return f'MyDefautDict({self.default_value}, {super().items()})'
    
    def __missing__(self, key):
        return self.default_value()