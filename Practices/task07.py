ATTRIBUTES = (
    '__module__',
    '__name__',
    '__qualname__',
    '__doc__',
    '__annotations__',
)

# ~ functools.wraps
def my_wraps(wrapped_function):

    def decorator(wrapper_function):    
        for attr in ATTRIBUTES:
            try:
                wrapped_attr = getattr(wrapped_function, attr)
            except AttributeError:
                pass
            else:
                setattr(wrapper_function, attr, wrapped_attr)

        return wrapper_function
            
    return decorator