# Задача 10: На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
coins = int(input('Quantity of coins? '))
coinStatus = input('Write down the current status, for example HTH mean Head, Teals, Head: ')

if coins != len(coinStatus):
    print('Error')
else:
    countHead = 0
    countTeals = 0
    for coin in coinStatus:
        if coin =='H':
            countHead += 1
        else:
            countTeals += 1

print(f'Minimum number of flips - {min(countHead,countTeals)}')