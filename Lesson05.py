# task01

import random

while True:

    guessed_number = random.randint(1, 10)
    gamer = input('guess the number from 1 to 10: ')
    if gamer == str(guessed_number):
        print('you guessed it')
    elif gamer == 'q':
        break
    else:
        print(f'you not guessed it, the answer', {guessed_number})

# task02

while True:

    name = input('Wot is your name?: ')
    if name == 'q':
        break
    age = input('Wot is your the age?: ')
    if age == 'q':
        break
    if not age.isnumeric():
        print('age is not a number')
        continue
    print(f"Hello", name.title(), "on your next birthday "
                                  "you’ll be", int(age) + 1, "years")

# task03

# strings = 'hello'
# counter = 0
# while counter <= 4:
#
#     print(random.choice(strings) + random.choice(strings)
#           + random.choice(strings) + random.choice(strings)
#           + random.choice(strings))
#     counter += 1

# strings = 'hello'
# counter = 0
# while counter <= 4:
#     print(random.choices(strings, k=len(strings)))
#     counter += 1

stings = input(' :')
counter = 0
listn = list(stings)
while counter <= 4:
    random.shuffle(listn)
    print(listn)
    counter += 1
