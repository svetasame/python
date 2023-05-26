
path = "phonebook.txt"

def read_file():
  data1= open(path, "r")
  for i in data1:
    print(i)
  data1.close()
    
def find_contact():
  data1= open(path, "r")
  flag = 1
  name = input ("Введите имя для поиска: ")    
  for line in data1:
    if name in line:
      flag = 0
      print (line)
    if flag ==1: print ("Имя не найдено")
    
def add_contact():
  data = open(path, "a")
  name = input("Введите имя: ").capitalize()
  second_name = input("Введите фамилию: ").capitalize()
  numb = input("Введите номер телефона: ")
  data.write(f"{name} {second_name}: {numb} \n")
  data.close()

# add_contact()
read_file()
find_contact()

# dict_defs = {"1": read_file, "2": find_contact, "3": add_contact}
# print('''Команды для работы со справочником:
#     Просмотр всех записей справочника: 1
#     Добавление новой записи: 3
#     Удаление записи из справочника по Имени и Фамилии:
#     Поиск по справочнику: 2
#     Изменить контакт: ''')

# while True:
#   command = input ("Команда: > ") 
#   if command in dict_defs:
#     dict_defs[command](path)
#   else:
#     print (" команды не существует")