contacts = []

def add_contact(name, phone, email):
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)

def show_all():
    for contact in contacts:
        print(f"Имя: {contact['name']}, Телефон: {contact['phone']}, Email: {contact['email']}")

def find_contact(query):
    result = []
    for contact in contacts:
        if query == contact["name"] or query == contact["phone"]:
            result.append(contact)
    return result

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
add_contact("Dinara", "+79174465420", "bikdifa@mail.ru")
save_contacts()
show_all()

load_contacts()

load_contacts()
