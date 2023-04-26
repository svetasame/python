# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def degree_a_b(a:int,b:int):
  if b == 1:
    return a
  elif b != 1:
    return (a*degree_a_b(a,b-1)) 

number = int(input("Введите число: "))
degree = int(input("Введите степень числа: "))
print("Результат возведения в степень равен: ", degree_a_b(number,degree))

# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4

def summ_of_num(a,b):
   if a == 0:
    return b
   return summ_of_num(a-1, b+1)

number_a = int(input("Введите первое число: "))
number_b = int(input("Введите второе число: "))
print("Сумма чисел равна: ",summ_of_num(number_a,number_b))