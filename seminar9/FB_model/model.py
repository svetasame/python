phone_book = []
path = "phone.txt"


def open_pb():
    global phone_book, path
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for contact in data:
        contact = contact.strip().split(":")
        phone_book.append({"name": contact[0], "phone": contact[1], "comment": contact[2]})


def get_pb() -> list[dict[str, str]]:
    global phone_book
    return phone_book

def add_contact(contact: dict[str, str]):
    global phone_book
    phone_book.append(contact)
    return contact.get("name")

def save_pb():
    global phone_book, path
    for contact in data:
        contact = contact.strip().split(":")
        phone_book.append({"name": contact[0], "phone": contact[1], "comment": contact[2]})
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(data)