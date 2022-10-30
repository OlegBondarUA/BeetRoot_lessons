import calendar
from datetime import datetime
from functools import wraps
from time import time


def average():
    my_list = []

    def inner(number):
        my_list.append(number)
        return sum(my_list) / len(my_list)

    return inner


def average_complex():
    my_list = []
    current = 0

    def inner(number):
        nonlocal current
        my_list.append(number)
        current = sum(my_list) / len(my_list)

    def value():
        return current

    def reset():
        nonlocal current
        current = 0
        my_list = []

    def set_current(number):
        nonlocal current
        current = number

    inner.value = value
    inner.reset = reset
    inner.set_current = set_current

    return inner


def first_decorator(function):
    def wrapper():
        print('Before function')
        function()
        print('After function')

    return wrapper


def say_hello_world():
    print('Hello world!!!')


def not_during_weekday(function):
    def wrapper():
        now = datetime.now()
        if calendar.weekday(now.year, now.month, now.day) \
                not in (calendar.SATURDAY, calendar.SUNDAY):
            function()
        print('Not weekend')

    return wrapper


def box_print(function):
    def wrapper():
        result = function()
        print('-' * (len(result) + 4))
        print('|', result, '|')
        print('-' * (len(result) + 4))

    return wrapper


@box_print
def say_hello_world_2():
    return 'Hello world!!!'


@box_print
def say_hello_oleg():
    return 'Hello Oleg!!!'


@box_print_3
def greet_person(name):
    return f'Hello {name}'


@box_print_3
def greet_person_with_age(name, age):
    return f'Hello {name}, your age {age}'


# def timer(function):
#     @wraps(function)
#     def wrapper(*args, **kwargs):
#         before = time()
#         result = function(*args, **kwargs)
#         after = time()
#         execution_time = after - before
#         print(f'{function.__name__} was executed in {execution_time:.4f} seconds')
#
#         return result
#
#     return wrapper


def timer(times):
    def inner(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            before = time()
            for _ in range(times - 1):
                function(*args, **kwargs)
            result = function(*args, **kwargs)
            after = time()
            execution_time = after - before
            print(
                f'{function.__name__} was executed in {execution_time:.4f} seconds')

            return result

        return wrapper

    return inner


# @timer
# def waste_some_time(number_of_times):
#     for _ in range(number_of_times):
#         sum(i ** 2 for i in range(10000))

@timer(5)
def greet_person_with_age(name, age):
    return f'Hello {name}, your age {age}'


def main():
    # price = average()
    #
    # price(100)
    # price(150)
    # price(200)
    # print(price(250))
    #
    # temp = average_complex()
    #
    # temp(25.0)
    # temp(21.0)
    # temp(24.0)
    # temp(30.0)
    # print(temp.value())
    #
    # temp.reset(10)
    #
    # print(temp.value())

    say = first_decorator(say_hello_world)
    # say()

    say = not_during_weekday(say_hello_world)

    # say()
    # say = box_print(say_hello_world)
    # say_hello_world_2()
    # say_hello_oleg()
    # greet_person('Nikolay')
    # result = greet_person_with_age('Lev', age=24)
    #
    # print(result)

    # print(greet_person_with_age)
    #
    # waste_some_time(999)

    greet_person_with_age('Oleg', 30)


if __name__ == '__main__':
    main()
