import json


class Contact:
    def __init__(self, full_name, phone_number):
        self.full_name = full_name
        self.phone_number = phone_number

    def to_dict(self):
        return {
            'full_name': self.full_name,
            'phone_number': self.phone_number
        }


class ContactList:
    def __init__(self):
        self.contacts = []

    def add_contact(self, full_name, phone_number):
        contact = Contact(full_name, phone_number)
        self.contacts.append(contact)

    def search_by_name(self, name):
        results = [contact for contact in self.contacts if name.lower() in contact.full_name.lower()]
        return results

    def import_from_json(self, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
            for item in data:
                self.add_contact(item['full_name'], item['phone_number'])

    def export_to_json(self, file_path):
        with open(file_path, 'w') as file:
            json.dump([contact.to_dict() for contact in self.contacts], file, indent=4)

    def display_all_contacts(self):
        for contact in self.contacts:
            print(f'Name: {contact.full_name}, Phone: {contact.phone_number}')


def main():
    contact_list = ContactList()

    while True:
        print("\n1. Add Contact")
        print("2. Search Contact by Name")
        print("3. Display All Contacts")
        print("4. Import Contacts from JSON")
        print("5. Export Contacts to JSON")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            full_name = input("Enter full name: ")
            phone_number = input("Enter phone number: ")
            contact_list.add_contact(full_name, phone_number)
            print("Contact added successfully!")
        elif choice == '2':
            name = input("Enter the name to search: ")
            results = contact_list.search_by_name(name)
            if results:
                print("Search results:")
                for contact in results:
                    print(f'Name: {contact.full_name}, Phone: {contact.phone_number}')
            else:
                print("No contacts found.")
        elif choice == '3':
            print("All contacts:")
            contact_list.display_all_contacts()
        elif choice == '4':
            file_path = input("Enter the file path to import contacts: ")
            contact_list.import_from_json(file_path)
            print("Contacts imported successfully!")
        elif choice == '5':
            file_path = input("Enter the file path to export contacts: ")
            contact_list.export_to_json(file_path)
            print("Contacts exported successfully!")
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")



ui = main()