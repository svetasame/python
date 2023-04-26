
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
# # вводим строку и переводим в список
# print(my_string)
# print(my_string[0], end=" ")
# # печатаем первый элемент
# for i in range(1, len(my_string)):
#   # считаем элементы с 1
#   print(f"{my_string[i]}", end=" ")
#   count = my_string[:i-1].count(my_string[i])
#   # делаем срез и считаем, увеличиваем каунт
#   # сразу без срезов нельзя потому что на момент вхождения
#   if count > 0:
#     print(f"_{count}", end=" ")


# my_string2 = list(input("Введите строку из символов: "))
# count_dict = {}
# for letter in my_string2:
#   count_dict[letter] = count_dict.get(letter, -1) + 1 
#   # берем из словаря то что там лежит до
#   #  если у нас есть значение - вернет, если нет то ноль
#   #  если уже лежало увеличиваем на 1
#   print(f"{letter}" if count_dict.get(letter) 
#         == 0 else f"{letter}_{count_dict.get(letter)-1}", end = " ")



# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# my_text = input("Введите текст: ").split()
# print (my_text)
# text_result = set()
# for word in my_text:
#   text_result.add(word.lower())
# print (len(text_result))


# **Задача 22:**
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит 
# сами элементы множеств.

import random
n = int(input("введите длину первого ряда чисел: "))
m = int(input("введите длину второго ряда чисел: "))
first_set = set()
both_in_two = set()
for i in range(n):
    i = random.randint(1, 10)
    print(i, end=" ")
    first_set.add(i)
print()
for i in range(m):
    i = random.randint(1, 10)
    print(i, end=" ")
    if i in first_set:
      both_in_two.add(i) 
print()       
print(sorted(both_in_two)) 


# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени 
# сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом 
# заданной во входном файле грядки.

import random
number_of_plants = int(input("введите количество кустов: "))
list_of_plants = list()
for i in range(number_of_plants):
  i = random.randint(1, 10)
  print(i, end=" ")
  list_of_plants.append(i)
  
max_to_bring = list()
for i in range(len(list_of_plants)-1):
  max_to_bring.append(list_of_plants[i-1]+list_of_plants[i]+list_of_plants[i+1])
max_to_bring.append(list_of_plants[-2]+list_of_plants[-1]+list_of_plants[0])
print()
print(max(max_to_bring))
