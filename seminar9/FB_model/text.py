main_menu = '''\nГлавное меню:
    1. Открыть файл
    2. Записать файл
    3. Показать контакт
    4. Добавить контакт
    5. Найти контакт
    6. Изменить контакт
    7. Удалить контакт
    8. Выход\n'''

input_choice = "Выберите пункт меню: "

load_successful = "Телефонная книга успешно открыта"

load_error = "Телефонная книга пуста или не открыта"

input_contact = {"name":"Введите имя: ",
                 "phone":"Введите телефон: ",
                 "comment":"Введите комментарий: "}

new_contact = "Введите данные нового контакта (пустое поле для отмены): "

def new_contact_successful(name: str) -> str:
    return f"Контакт {name} успешно добавлен"

cancel_input = "Отмена ввода"

save_successful = "Телефонная книга успешно сохранена"

input_del_index = "Введите индекс контакта для удаления: "

def del_contact(name: str):
    return f"Контакт {name} успешно удален!"

input_find = "Что будем искать: "

input_change = "Введите контакт для изменения: "

input_index = "Введите индекс контакта: "


def contact_is_not_found(word) -> str:
    return f"Контакты, содержащие {word} не найдены!"

def change_successful (name: str):
    return f"Контакт {name} успешно изменен!"

change_contact = "Введите новые данные или оставьте поля пустыми, чтобы не менять: "
