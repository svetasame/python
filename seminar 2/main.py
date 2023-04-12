
my_limit = int (input('Введите предел факториала: '))

fact = 1
count = 1 
while count <= my_limit:
    fact *=count
    count +=1

print(f"Факториал числа {my_limit} = {fact}")
  