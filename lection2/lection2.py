# list_1 = []
# list_1 = list()
# list_1 = [1,2,3,8]
# print(*list_1)

# поиск элементов в списке
# for i in list_1:
#   print (i)


# # найти длину списка
# print(len(list_1))

# # индексация с конца
# print(list_1[-1])

# добавить цифру в конец списка
# list_2 =[1,5]
# print(list_2)
# list_2.append(8)
# print(list_2)

# поочередно добавили значения в список
# list_1 = []
# print(list_1)
# for i in range(5):
#   list_1.append(i)
#   print(list_1)
  
#  возвращение последнего значения
# list_1 = [1,2,3,8]
# print(list_1.pop())
# a = list_1.pop()

# удаление конкретного элемента
# print(list_1.pop(0))
# print(list_1)

# добавление элемента на нужную позицию
# list_1 = [1,2,3,8]
# print(list_1.insert(2,11))
# print(list_1)

# срезы - положительная и отрицательная индексация
# значение через :
#   если перед ничего нет начинаем сначала
#   если перед : 2 то сначала и до 2 не вкл
#   такж можем два последних
# list_1 = [1,2,3,8]

# определить класс кортеж
# t = ()
# print(type(t))

# t = (1, )
# print(type(t))

# v = [1, 8, 5, 6]
# print (v)
# print(type(v))
# # преобразование
# v = tuple(v)
# print (type(v))

# # множественное присваивание
# a,b,c,d = v
# x,z = 1,2

# print(a,b,c)

# создать словарь
# d = {}

# d = dict()
# d ['q'] = 'qwerty'
# print(d)

# d ['w'] = 'werty'
# print(d)

# множество - в словаре ключ и значение, тут просто значение
# colors = {'red', 'green', 'blue'}
# print(colors)
# colors.add('gray')
# print(colors)
# colors.remove('red') 
# # удалить значение которое точно нет
# print(colors)
# colors.discard('red') 
# print(colors)
# удалить если мы не знаем есть или нет

# Операции со множествами в Python:
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13,
# i = a.intersection(b) # i = {8, 2, 5}
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}
# q = a.union(b).difference(a.intersection(b))# {1, 21, 3, 13}
# a = {1,2,3}
# b= frozenset(a)
# # замороженное множество

# list_1 = [exp for ite, in iterable]
# list_1 = [exp for item in iterable (if conditional)]
# создать список классика
list_1 = []
for i in range(1,11):
  list_1.append(i)
print(list_1)  
  
# создать список альтернативно
list_2 = [i for i in range(1,11)]
print(list_2) 

# список с условием, например четные числа
list_3 = [i for i in range(1,11) if i%2==0]
print(list_3) 
