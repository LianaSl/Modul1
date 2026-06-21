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

add_contact("Dinara", "+79174465420", "bikdifa@mail.ru")
for contact in contacts:
    print(contact)