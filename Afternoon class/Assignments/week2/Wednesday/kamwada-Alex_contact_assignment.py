
contacts = []


def validate_phone(phone):
    if not all(c.isdigit() or c in '-+' for c in phone):
        print("Error: Phone number must contain only digits, hyphens, or '+'.")
        return False
    return True


def validate_email(email):
    if email and ('@' not in email or '.' not in email):
        print("Error: Email must contain '@' and '.'.")
        return False
    return True


def add_contact(name, phone, email=""):
    if not validate_phone(phone):
        return
    if not validate_email(email):
        return
    contacts.append({"name": name, "phone": phone, "email": email})
    print(f"Contact '{name}' added successfully.")


def view_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print(f"\nName : {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email'] or 'N/A'}")
            return
    print(f"Contact '{name}' not found.")


def update_contact(name, new_phone=None, new_email=None):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            if new_phone is not None:
                if not validate_phone(new_phone):
                    return
                contact["phone"] = new_phone
            if new_email is not None:
                if not validate_email(new_email):
                    return
                contact["email"] = new_email
            print(f"Contact '{name}' updated successfully.")
            return
    print(f"Contact '{name}' not found.")


def delete_contact(name):
    for i, contact in enumerate(contacts):
        if contact["name"].lower() == name.lower():
            contacts.pop(i)
            print(f"Contact '{name}' deleted.")
            return
    print(f"Contact '{name}' not found.")


def search_contacts(query):
    query_lower = query.lower()
    results = [
        c for c in contacts
        if query_lower in c["name"].lower()
        or query_lower in c["phone"]
        or query_lower in c["email"].lower()
    ]

    if not results:
        print(f"No contacts found matching '{query}'.")
        return

    print(f"\n--- Search Results for '{query}' ({len(results)} found) ---")
    for i, c in enumerate(results, 1):
        print(f"{i}. {c['name']}")
        print(f"   Phone: {c['phone']}")
        print(f"   Email: {c['email'] or 'N/A'}")
    print("-------------------------------------------")


def list_all_contacts():
    if not contacts:
        print("No contacts saved yet.")
        return

    print(f"\n{'#':<5} {'Name':<20} {'Phone':<20} {'Email'}")
    print("-" * 65)
    for i, c in enumerate(contacts, 1):
        print(f"{i:<5} {c['name']:<20} {c['phone']:<20} {c['email'] or 'N/A'}")
    print("-" * 65)


def main():
    while True:
        print("\n=== Contact Manager Menu ===")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contacts")
        print("6. List All Contacts")
        print("7. Exit")

        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            name = input("Name: ").strip()
            phone = input("Phone: ").strip()
            email = input("Email (optional, press Enter to skip): ").strip()
            add_contact(name, phone, email)

        elif choice == "2":
            name = input("Enter name to view: ").strip()
            view_contact(name)

        elif choice == "3":
            name = input("Enter name to update: ").strip()
            new_phone = input("New phone (press Enter to skip): ").strip() or None
            new_email = input("New email (press Enter to skip): ").strip() or None
            update_contact(name, new_phone, new_email)

        elif choice == "4":
            name = input("Enter name to delete: ").strip()
            delete_contact(name)

        elif choice == "5":
            query = input("Search query (name, phone, or email): ").strip()
            search_contacts(query)

        elif choice == "6":
            list_all_contacts()

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose between 1 and 7.")


if __name__ == "__main__":
    main()
