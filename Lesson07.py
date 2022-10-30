# task01

def text(texts):
    counts = dict()
    text1 = texts.split()

    for i in text1:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1

    return counts


print('Слова та їхня кількість', text('You saw above that when you assign a value to an already existing dictionary'
                                      'key, it does not add''the key a'' second time, but replaces the existing value'))

# task02

stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}
prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
prices1 = sum(stock[fruit] * prices[fruit] for fruit in prices)
for x in stock:
    prices[x] = prices[x] * stock[x]


print(prices)
print('Спільна сума', prices1)


# task03

nev_list = []
d = []
z = []
for n in range(2, 9):

    d.append(str(n))
    z.append(str(n ** 2))
nev_list.append(tuple(d))
nev_list.append(tuple(z))
print('Кортеж + Кортеж^2', nev_list)

j = [(x, x ** 2) for x in range(2, 9)]

print(j)
