# task 01

def oops(*arg):
    try:
        print('\n', arg[5])
    except IndexError:
        print('\nno index oops error')


oops(1, 5, 2, 0, 3)


# task 02

def numbers():
    try:
        a = int(input('Введіть значення A:'))
        b = int(input('Введіть значення B:'))
        x = a // b
        print('\n', x)
    except ValueError:
        print('Please enter the numbers')
    except ZeroDivisionError:
        print('t is not possible to divide by 0')


numbers()
