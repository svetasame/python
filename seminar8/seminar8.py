path = "phonebook.txt"

# показать справочник
def read_file():
  data1 = open(path, "r")
  for i in data1:
    print(i)
  data1.close()

# найти контакт в справочнике
def find_contact():
  data1 = open(path, "r")
  name = input("Введите имя для поиска: ")
  for line in data1:
    if name in line:
      print(line)
      break
  else:
    print("Имя не найдено")
  data1.close()

# изменить контакт
def change_contact():
  data1 = open(path, "r+")
  data_new = data1.readlines()
  name = input("Введите имя для изменения: ")
  data1.seek(0)
  for line in data_new:
    if name in line:
      print("Вы хотите изменить контакт %s (yes/no)?: " % name)
      change_name = input("Введите yes/no: ")
      if change_name == "yes":
        name_new = input("Введите имя: ").capitalize()
        second_name = input("Введите фамилию: ").capitalize()
        numb = input("Введите номер телефона: ")
        data1.write(f"{name_new} {second_name}: {numb} \n")
    else:
      data1.write(line)
  print("Вы изменили контакт %s " % name)
  data1.close()

# удалить контакт
def del_contact():
  data1 = open(path, "r+")
  data_new = data1.readlines()
  data1.seek(0)
  name = input("Введите имя для удаления: ")
  for line in data_new:
    if name not in line:
      data1.write(line)
  data1.truncate()
  print("Вы удалили контакт %s \n" % name)
  data1.close()

# добавить контакт
def add_contact():
  data = open(path, "a")
  name = input("Введите имя: ").capitalize()
  second_name = input("Введите фамилию: ").capitalize()
  numb = input("Введите номер телефона: ")
  data.write(f"{name} {second_name}: {numb} \n")
  data.close()

dict_defs = {"1": read_file, "2": find_contact,
             "3": add_contact, "4": change_contact,
             "5": del_contact}

print('''Команды для работы со справочником:
    Просмотр всех записей справочника: 1
    Найти контакт в справочнике: 2
    Добавить новый контакт в справочник: 3
    Изменить контакт в справочнике: 4
    Удалить контакт в справочнике: 5''')

while True:
  command = input("Введите команду: ")
  if command in dict_defs:
    dict_defs[command]()
  else:
    print("Данной команды не существует")
