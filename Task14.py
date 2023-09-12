# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
N = int(input('Введите число N: '))
resOfDegree = 0
degree = 0  # Инициализируем degree до цикла
while resOfDegree <= N:
    resOfDegree = 2 ** degree
    if resOfDegree > N:
        break
    else:
        degree += 1
        print(resOfDegree)