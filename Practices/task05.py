import contextlib

@contextlib.contextmanager
def suppress(*args):
    print('Suppress starts')
    try:
        yield
    except args as ex:
        print(repr(ex))
    print('Suppress ends')

with suppress(KeyError, IndexError):
   {}[1]