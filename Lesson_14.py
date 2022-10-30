from functools import wraps


def logger(function):
    @wraps(function)
    def wrap(*args, **kwargs):
        print(function.__name__, 'called with', *args, **kwargs)
    return wrap


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

###############################################################################


def stop_words(words: list):
    def inner(function):
        @wraps(function)
        def wrap(*args, **kwargs):
            res_func = function(*args, **kwargs)
            for word in words:
                res_func = res_func.replace(word, '*')
            return res_func
        return wrap
    return inner


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


##############################################################################


def arg_rules(type_: type, max_length: int, contains: list):
    def inner(function):
        @wraps(function)
        def wrap(s, *args, **kwargs):
            if isinstance(s, type_):
                function(s, *args, **kwargs)
            else:
                return False
            if len(str(s)) > max_length:
                return False
            if contains == ['05', '@']:
                function(s, *args, **kwargs)
            else:
                return False

            return function(s, *args, **kwargs)
        return wrap
    return inner


@arg_rules(type_=str, max_length=7, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

##############################################################################


def box_print_super(arg, line):
    def inner(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            print(arg * (line + 4))
            for i in range(0, len(result), line):
                print(arg, result[i:(i + line)], arg)
            print(arg * (line + 4))
            print(arg * (len(result) + 4))
            print(arg, result, arg)
            print(arg * (len(result) + 4))
            return result

        return wrapper
    return inner


@box_print_super('#', 7)
def greet_person_with_age(name, age):
    return f'Hello {name}, your age {age}'


def main():
    # task 01
    print()
    add(4, 5)
    square_all(2, 4, 5, 6)
    # task 02
    print()
    print(create_slogan('Oleg'))
    print()
    print(create_slogan('Petrovichteh@gmail.com'))
    print(create_slogan('S@SHA05'))
    # task 04
    print()
    greet_person_with_age('Oleg',  '31'.center(5))


if __name__ == '__main__':
    main()
