
# дз другой вариант
# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1
# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

# import random
# n = int(input('Введите размер списка: '))
# numbers = [random.randint(-10, 10) for _ in range(n)]
# print(numbers)
# x = int(input('Введите число для поиска: '))
# count = numbers.count(x)  # посчитать сколько раз число встречается в списке
# closest = numbers[0]
# if count < 1:
#     for item in numbers:
#       if abs(x-item) < abs(x-closest):
#         closest = item
# print(f'число {x} встречается в списке {count} раз' if count >= 1
#       else f'ближайшее число к {x} = {closest}')

# Задача 20: В настольной игре Скрабл (Scrabble) другой вариант решения

# scrabble = {1: 'AEIOULNSTRАВЕИНОРСТaeioulnstrавеинорст', 2: 'DGДКЛМПУdgдклмпу', 
#             3: 'BCMPБГЁЬЯbcmpбгёья', 4: 'FHVWYЙЫfhvwyйы', 
#             5: 'KЖЗХЦЧkжзхцч', 8: 'JXШЭЮjxшэю', 10: 'QZФЩЪqzфщъ'}
# word = input('Введите слово: ')
# total = 0

# for letter in word.upper():
#   for points, letters in scrabble.items(): #проходимся по ключам и значениям
#     if letter in letters:
#       total += points
#       break
# print(f'Слово "{word}" весит {total} баллов')

# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

# my_string = list(input("Введите строку из символов: "))
# print(my_string)
# print(my_string[0], end=" ")
# for i in range(1, len(my_string)):
#   print(f"{my_string[i]}", end=" ")
#   count = my_string[:i-1].count(my_string[i])
#   if count > 0:
#     print(f"_{count}", end=" ")
