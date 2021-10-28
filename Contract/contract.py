class ContractError(Exception):
    """We use this error when someone breaks our contract."""


#: Special value, that indicates that validation for this type is not required.
class AnyClass(object):
    def __eq__(self, _):
        return True

Any = AnyClass()


def contract(arg_types=None, return_type=None, raises=None):
    '''
    :usage:
        `arg_types = None`        - without any checks
        `arg_types = (int,)`      - only one argument must have `int` type
        `arg_types = (str, Any)`  - first argument must have `str` type
                                    second argument can have any type

        `return_type = None`      - without any checks
        `return_type = float`     - result must have `float` type
        `return_type = Any`       - result can have any type

        `raises = None`                     - without any checks
        `raises = (ValueError, TypeError)`  - function can raise ValueError and TypeError

    :raises:
        ContractError if the conditions are not met
    '''

    def decorator(function):

        def validate_arg_types(actual_arg_types):
            if arg_types is None:
                return
            if arg_types != actual_arg_types:
                raise ContractError(
                    f'Wrong argument types: expected = {arg_types}, but actual = {actual_arg_types}'
                )

        def validate_return_type(actual_return_type):
            if return_type is None:
                return
            if return_type != actual_return_type:
                raise ContractError(
                    f'Wrong return type: expected = {return_type}, but actual = {actual_return_type}'
                )

        def validate_raises(code):
            if raises is not None:
                try:
                    result = code()
                except raises:
                    raise
                except Exception as ex:
                    raise ContractError('Unexpected error') from ex
            else:
                result = code()

            return result, type(result)

        def wrapper(*args):
            actual_arg_types = tuple(map(type, args))
            validate_arg_types(actual_arg_types)

            result, actual_return_type = validate_raises(lambda: function(*args))
            validate_return_type(actual_return_type)

            return result

        return wrapper

    return decorator
