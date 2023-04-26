def fibo(n):
  if n == 0 or n == 1:
    return 1
  return fibo(n - 1) + fibo(n - 2)
  
  
  
# print(fibo(6))


# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

import random
# grades = int(input("введите количество оценок: "))
# list_of_grades = [random.randint(1, 5) for _ in range(grades)]
# print(list_of_grades)
# max_grade = max(list_of_grades)
# min_grade = min(list_of_grades)
# print("максимальное и минимальное числа: ",max_grade,min_grade) 
# for i in range(len(list_of_grades)): 
#   if list_of_grades[i] == max_grade:
#     list_of_grades[i] = min_grade
# print(list_of_grades)   
 
# задаем список в одну строчку  
# print(mark_list := [random.randint(1,5) for _ in range (10)])
# print(mark_list := [min(mark_list) if i == max(mark_list) 
#                     else i for i in mark_list])
# тернарный опреатор

# Задача №35. Общее обсуждение
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes


def simple_digit(n):
  if n < 2:
    return False
  for i in range(2, int(n** 0.5)+1):
    if n % i == 0:
      return False
  return True
 
def simple_digit2(n):
  count = 0
  for i in range(1, n+1):
    if n % i == 0:
      count +=1
  if count == 2 or n == 1 or n == 2:
    print("yes")
  else:
    print("no")
    
def is_simple(n: int) -> bool:
  if n in [1,2]:
    return True
  elif not n%2:
    return False
  for i in range(3, n // 2 + 1, 2):
    if n %i == 0:
      return False
  return True
# n = int(input("Введите число: "))
# print(f'Число {n} ' + ('простое' if is_simple(n) else 'комплексное'))
# print(simple_digit(int(input("Введите число: "))))
# simple_digit2(int(input("Введите число: ")))

# Задача №37. 
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

# quant = int(input("введите количество чисел: "))
# list_of_numbers = [random.randint(1, 5) for _ in range(quant)]
# print(list_of_numbers)
# list_of_numbers.reverse()
# print(list_of_numbers)

def reverse_string(string):
  if len (string) == 0:
    return string
  else:
    return reverse_string(string[1:]) + string [0]

print(a := input ("Введите последовательность: "))
print(reverse_string(a))
  