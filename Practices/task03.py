def raiseSystemExit():
    try:
        exit(0)
    except SystemExit as ex:
        print(f'{ex = }')

def raiseKeyboardInterrupt():
    input() # press Ctrl+C

def raiseGeneratorExit():
    def generate():
        try:
            yield
        except GeneratorExit as ex:
            print(f'{ex = }')
    next(generate())

def raiseStopIteration():
    def generate():
        if False:
            yield
    next(generate())

# raiseStopAsyncIteration ???

def raiseFloatingPointError():
    import numpy as np
    with np.errstate(invalid='raise'):
        np.sqrt(-1)

def raiseOverflowError():
    10.1 ** 10000

def raiseZeroDivisionError():
    1 // 0

def raiseAssertionError():
    assert 1 == 0

def raiseAttributeError():
    None.name

def raiseBufferError():
    from io import BytesIO
    array = BytesIO(b'0')
    _ = array.getbuffer()
    array.write(b'1')

def raiseEOFError():
    input() # press Ctrl+Z (win), Ctrl+D (linux)

def raiseImportError():
    from sys import a

'''
def raiseModuleNotFoundError():
    import python4
'''

def raiseIndexError():
    [][0]

def raiseKeyError():
    {}[0]

def raiseMemoryError():
    '0' * 10 ** 12

'''
def raiseNameError():
    a
'''

'''
def raiseUnboundLocalError():
    a = 1
    def f(): 
        if a > 0:
            ...
        a = -1
    f()
'''

# skip all OSError's

def raiseReferenceError():
    from weakref import proxy

    class A: ...

    a = A()
    ref = proxy(a)
    del a
    print(ref)

def raiseNotImplementedError():
    import os
    os.PathLike.__fspath__(1)

def raiseRecursionError():
    def f():
        return f()
    f()

def raiseSyntaxError():
    '''
    ,
    '''
    ... # ^ uncomment it

def raiseIndentationError():
    '''
    a = 0
     b = 0
    '''
    ... # ^ uncomment it

def raiseTabError():
    '''
    a = 0 # 4 spaces
	b = 0 # 1 tab
    '''
    ... # ^ uncomment it

# SystemError ???

def raiseTypeError():
    len(1)

def raiseValueError():
    from math import log2
    log2(0)

def raiseUnicodeDecodeError():
    b'\x99'.decode('utf-8')

def raiseUnicodeEncodeError():
    'ж'.encode('ascii')

# UnicodeTranslateError ???