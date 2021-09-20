from functools import wraps


def log(function):
    @wraps(function)
    def decorator(*args, **kwargs):
        name = decorator.__name__
        args_values = list(map(str, args))
        kwargs_values = [
            f'{name} = {value}' for name, value in kwargs.items()
        ]
        all_args = ', '.join(args_values + kwargs_values)
        
        print(f'{name}({all_args}) ...')
        result = function(*args, **kwargs)
        print(f'{name}({all_args}) = {result}')
        
        return result
    
    return decorator


@log
def sample_function(a, b):
    return a ** 2 + b ** 2


if __name__ == '__main__':
    sample_function(2, b = 1)