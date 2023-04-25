# def sumnumbers(n, y = "hell"): # считает сумму чисел до числа н 5 - 15 6 - 16
#   summ = 0
#   print(y)
#   for i in range(1, n+1): #начинаем с 1, 
#     summ +=i
#   # print(summ)
#   return(summ) # завершает работу функиции

# a = sumnumbers(6, "gift")  
# print(a)
# # print(sumnumbers(6))

# def sum_str(*args):
#   res = ""
#   for i in args:
#     res+=i
#   return res

# print(sum_str("g","i","f",'t'))

# import modul1
# print(modul1.max1(5,9))

# from modul1 import max1
# print(max1(1,10))

# from modul1 import *
# print(max1(5,4))

import modul1 as m1
# print(m1.max1(5,6))

# list_1 = []
# for i in range(1, 10):
#   list_1.append(m1.fibb(i))
# print(list_1)

# print(m1.quick_sort([1,2,3,4,5,9,8,9]))

list_2 = [1,10,5,6,7,2,6]
m1.merge_sort(list_2)
print(list_2)