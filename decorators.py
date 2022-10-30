from functools import wraps


def box_print(function):

    def wrapper():
        result = function()
        print('-' * (len(result) + 4))
        print('|', result, '|')
        print('-' * (len(result) + 4))

    return wrapper


def box_print_2(function):

    def wrapper(name, age):
        result = function(name, age)
        print('-' * (len(result) + 4))
        print('|', result, '|')
        print('-' * (len(result) + 4))

    return wrapper


def box_print_3(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        print('-' * (len(result) + 4))
        print('|', result, '|')
        print('-' * (len(result) + 4))
        return result

    return wrapper


def decorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        # Do something before
        result = function(*args, **kwargs)
        # Do something after
        return result

    return wrapper
