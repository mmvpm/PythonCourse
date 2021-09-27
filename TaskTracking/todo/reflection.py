import inspect
import sys


def find_classes(base_class) -> tuple:
    """
    Finds all subclasses of a class inside module.

    :param base_class: Base class to search children.
    :return: tuple of subclasses
    """
    return inspect.getmembers(
        sys.modules[base_class.__module__],
        _reflect_filter(base_class),
    )


def _reflect_filter(base_class):
    """
    Reflection is used to load modules dynamically.

    This method is complex. It does some dark magic.
    How is it even possible to understand it?

    :param base_class: Target base class
    :return: function to filter only subclasses of `base_class`
    """
    def class_filter(klass):
        return inspect.isclass(
            klass,
        ) and klass.__module__ == base_class.__module__ and issubclass(
            klass, base_class,
        ) and klass is not base_class
    return class_filter
