contacts = []

def add_contact(name, phone, email):
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)

def show_all():
    for contact in contacts:
        print(f"Имя: {contact['name']}, Телефон: {contact['phone']}, Email: {contact['email']}")

def find_contact(query):
    result = filter(lambda c: c["name"] == query or c["phone"] == query, contacts)
    return list(result)

def delete_contact(query):
    for contact in contacts:
        if query == contact["name"] or query == contact["phone"]:
            contacts.remove(contact)
            return True
    return False

def update_contact(query, new_name, new_phone, new_email):
    for contact in contacts:
        if query == contact["name"] or query == contact["phone"]:
            contact["name"] = new_name
            contact["phone"] = new_phone
            contact["email"] = new_email
            return True
    return False

def save_contacts():
    with open("contacts.txt", "w", encoding="utf-8") as f:
        for contact in contacts:
            f.write(f"{contact['name']},{contact['phone']},{contact['email']}\n")

def load_contacts():
    try:
        with open("contacts.txt", "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(",")
                contact = {"name": parts[0], "phone": parts[1], "email": parts[2]}
                contacts.append(contact)
    except FileNotFoundError:
        pass

load_contacts()

while True:
    print("\n1. Добавить контакт")
    print("2. Найти контакт")
    print("3. Удалить контакт")
    print("4. Обновить контакт")
    print("5. Просмотреть контакты")
    print("6. Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        name = input("Имя: ")
        phone = input("Телефон: ")
        email = input("Email: ")
        add_contact(name, phone, email)
        save_contacts()
        print("Контакт успешно добавлен!")

    elif choice == "2":
        query = input("Введите имя или телефон: ")
        result = find_contact(query)
        if result:
            for contact in result:
                print(f"Имя: {contact['name']}, Телефон: {contact['phone']}, Email: {contact['email']}")
        else:
            print("Контакт не найден.")

    elif choice == "3":
        query = input("Введите имя или телефон: ")
        if delete_contact(query):
            save_contacts()
            print("Контакт удалён!")
        else:
            print("Контакт не найден.")

    elif choice == "4":
        query = input("Введите имя или телефон: ")
        new_name = input("Новое имя: ")
        new_phone = input("Новый телефон: ")
        new_email = input("Новый email: ")
        if update_contact(query, new_name, new_phone, new_email):
            save_contacts()
            print("Контакт обновлён!")
        else:
            print("Контакт не найден.")

    elif choice == "5":
        sorted_contacts = sorted(contacts, key=lambda c: c["name"])
        for contact in sorted_contacts:
            print(f"Имя: {contact['name']}, Телефон: {contact['phone']}, Email: {contact['email']}")

    elif choice == "6":
        print("Программа завершена. До свидания!")
        break

    else:
        print("Неверный выбор. Попробуйте снова.")