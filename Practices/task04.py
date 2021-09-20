from random import randint

class RandomStringGenerator(object):

    def __init__(self, length):
        if length % 2 != 0:
            raise ValueError('length should be divided by 2')
        self._half_length = length // 2
        self._prefix = self._get_random_string()
        self._suffix = self._get_random_string()

    def _get_random_char(self):
        return chr(randint(33, 127))
    
    def _get_random_string(self):
        return ''.join(
            self._get_random_char() for _ in range(self._half_length)
        )

    def __iter__(self):
        return self
    
    def __next__(self):
        self._prefix = self._suffix
        self._suffix = self._get_random_string()
        return self._prefix + self._suffix


generator = RandomStringGenerator(6)
for i in range(10):
    print(next(generator))