
# my_limit = int (input('Введите предел факториала: '))

# fact = 1
# count = 1 
# while count <= my_limit:
#     fact *=count
#     count +=1

# print(f"Факториал числа {my_limit} = {fact}")

# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.


# n0 = 0
# n1 = 1
# fib_n = int(input("Введите число А > 1: "))
# result = 0
# count = 1
# while result < fib_n:
#     result = n0 + n1
#     n0 = n1
#     n1 = result
#     count += 1
# if result == fib_n:
#     print(
#         f"число {fib_n} является {count} по счету в последовательности Фибоначчи")
# else:
#     print("-1")


# n0 = 0
# n1 = 1
# fib_n = int(input("Введите число А > 1: "))
# count = 2
# while n1 < fib_n:
#     n0, n1 = n1, n1+1 # упростили себе жизнь
#     count += 1
# # if n1 == fib_n:
# #     print(f"число {fib_n} является {count} по счету в последовательности Фибоначчи")
# # else:
# #     print("-1")
# print(count if n1 == fib_n else -1)


# Задача №13. Решение в группах
# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

# import random
# length = 30
# count = 0
# max_count = 0
# temp = 0
# for i in range(length): # range создает последовательность из числа
#     temp += random.randint(-3, 3)
#     print(temp, end=" ")
#     if temp > 0:
#         count += 1
#         if count > max_count:
#             max_count = count
#     else:
#         count = 0
# print(f"\n {max_count} - количество дней с оттепелью")



# Задача №15. Решение в группах
# Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

import random
MAX_WEIGHT = 9 # используем инвертируемые константы
MIN_WEIGHT = 1

quantity = int(input ("введите количество арбузов: "))
max_weight = MIN_WEIGHT
min_weight = MAX_WEIGHT
for i in range(quantity):
    weigth = random.randint(1, 9)
    print(weigth, end=" ") # распечатка в строку через пробел
    if  weigth > max_weight:
        max_weight = weigth
    if weigth < max_weight:
        min_weight = weigth
print(f"\n{max_weight} - самый тяжелый арбуз, {min_weight} - самый легкий")

