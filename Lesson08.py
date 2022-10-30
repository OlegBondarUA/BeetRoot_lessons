# task 01
def favorite_movie(name):
    print('\nMy favorite movie is named', name, '\n')


favorite_movie('Avengers')


# task 02

def make_country(country, capital):
    dictionary = dict()

    for x in country, capital:
        if x in dictionary:
            dictionary[x] += capital
        else:
            dictionary[x] = capital
        return dictionary


print(make_country(country='Ukraine', capital='Kyiv'))
print(make_country(country='USA', capital='Washington'))
print(type(make_country(country='Ukraine', capital='Kyiv',)))

# task 03


def make_operation(*args):
    operator = args[0]
    result = args[1]
    for n in args[2:]:
        if operator == '+':
            result += n
        if operator == '-':
            result -= n
        if operator == '*':
            result *= n
    return result


print(make_operation('+', 7, 8, 7))
print(make_operation('-', 5, 5, -10, -20))
print(make_operation('*', 7, 6))
