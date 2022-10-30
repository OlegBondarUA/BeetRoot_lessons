# task01
import random
i = 1
while i <= 5:
    lst = [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100),
           random.randint(1, 100), ]

    print('list of numbers', lst)
    print('maximum number', max(lst))
    i = i + 1

# task02
lst = []
lst02 = []
lst03 = []
i = 1
while i <= 5:
    lst.append(random.randint(1, 100))
    lst02.append(random.randint(1, 100))
    i = i + 1
    lst03.extend(lst + lst02)
print(' random numbers', lst, '\n', 'random numbers', lst02)
print('2 lists without oaks', set(lst03))


# task03

lst = []
for lst2 in range(1, 101):
    if lst2 % 7 == 0:
        lst.append(lst2)
print('list % 7', lst)
