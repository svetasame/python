# map

# my_string = "12345gbhbeas6"
# # my_string = list(map(int, my_string))
# print(my_string)

# # filter - проверяет и фильтрует 

# def is_digit(num: str):
#   if num.isdigit():
#     return True
#   return False

# my_string = list(map(int,filter(is_digit,my_string)))
# print(my_string)


# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна
# Пример ввода и вывода данных представлены на
# следующем слайде
from math import pi
import random

orbits_1 = [(3, 4), (6, 9), (12, 3), (9, 5), (7, 7), (8, 13)]


# size = int(input("Введите список планет: "))
# orbits = [(random.randint(1, 10), random.randint(1, 10)) for i in range(size)]
# print(orbits)

def find_farthest_orbit(list_of_orbits: list) -> tuple:
  dict_ = {round(pi*orbit[0]/2 * orbit[1]/2, 2): orbit for orbit in
           filter(lambda orbit: orbit[0] != orbit[1], list_of_orbits)}
  return dict_

# dict_p = find_farthest_orbit(orbits)
# print(max(dict_p), dict_p[max(dict_p)])



# Задача №51. Решение в группах
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод: Вывод:
# values = [0, 2, 10, 6] same
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)

quant = int(input("Введите количество объектов: "))
objects = [random.randint(1, 10) for i in range(quant)]
print(objects)

def same_by(characteristic, values):
  my_set = set(map(characteristic, values))
  return len(my_set) < 2
   

print(same_by(lambda values: values%2, objects))