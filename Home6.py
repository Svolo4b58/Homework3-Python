# Задача 30 Заполните массив элементами арифметической прогрессии. Её первый элемент, разность 
# и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки

# a1 = int(input('Первое число: '))
# d = int(input('Второе число: '))
# n = int(input('Третье число: '))
# for i in range(n):
#     print(a1 + i * d)

# Задача 32Определить индексы элементов массива (списка), значения которых принадлежат заданному 
# диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

# list = [-3, 7, 0, 4, -2, -5, 3, 6, -5, 12, 3, 1, -7, 11, 4, -9, 0, -3, -6, 4]
# m = int(input('Введите нижний предел: '))
# n = int(input('Введите верхний предел: '))
# for i in range(len(list)):
#     if m <= list[i] <= n:
#         print(i)