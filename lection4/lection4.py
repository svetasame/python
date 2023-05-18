import random
# def f(x):
#   return x*x

# print (f(5))
# print (type(f))

# a = f

# print(type(a))


def calc1(a, b):
  return a+b
# запись первая


def calk1(a, b): return a+b
# запись вторая сокращенная


def calc2(a, b):
  return a*b


def math(op, x, y):
  print(op(x, y))

# math(calc1, 5, 45)

# math(lambda a,b: a+b, 5, 45)


def new_list(msg):
  size = int(input(msg))
  list = [random.randint(1, 10) for _ in range(size)]
  return list


def parity_check(list1):
  parity_list = list()
  for i in list1:
    if i % 2 == 0:
      parity_list.append((i, i**2))  # передать значения в виде кортежа
  return parity_list


def select(f, col):
  return [f(x) for x in col]

def where(f, col):
  return [x for x in col if f(x)]

# list_1 = new_list("Введите размер первого массива: ")
list_2 = [1, 2, 2, 6, 3, 7, 9, 10]
res = map(int, list_2)
# print(res)
res = filter(lambda x: x % 2 == 0, res)
# print(res)
res = list(map(lambda x: (x, x**2), res))
# print(res)
# print(list_1, parity_check(list_1), sep="\n")

list_3 = [x for x in range(1, 20)]
# print(list_3)

list_3 = list(map(lambda x: x + 10, list_3))
# функция map передаем в параметрах два значения - ФУНКЦИЯ к каждому обьекту и сам обьект 
# print(list_3)

# .split() - преваращает строку в список

data = "15 20 30 40 5 65 4"
# print(data)

data = list(map(int,data.split()))
# print(data)

data_1 = [15, 20, 30, 40, 5, 65, 4]
res_1 = list(filter(lambda x: x%10 == 5, data_1))
# print(res_1)

users = ['user1','user2','user3','user4', 'user5']
ids = [4,5,9,14,7]
data_4 = list(zip(users,ids))
# print(data_4)

goroda = ['lasvegas','vladivostok','moscow']
print(list(enumerate(goroda)))
