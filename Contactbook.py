class Contact:
    def _init_(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def _init_(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. {contact.name} - {contact.phone}")

    def search_contact(self, search_term):
        found_contacts = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        if not found_contacts:
            print("No contacts found.")
        else:
            for contact in found_contacts:
                self.display_contact(contact)

    def update_contact(self, search_term):
        found_contacts = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        if not found_contacts:
            print("No contacts found.")
        else:
            contact = found_contacts[0]
            self.display_contact(contact)
            name = input("Enter new name (leave blank to keep current): ") or contact.name
            phone = input("Enter new phone (leave blank to keep current): ") or contact.phone
            email = input("Enter new email (leave blank to keep current): ") or contact.email
            address = input("Enter new address (leave blank to keep current): ") or contact.address
            contact.name, contact.phone, contact.email, contact.address = name, phone, email, address
            print("Contact updated successfully.")

    def delete_contact(self, search_term):
        found_contacts = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        if not found_contacts:
            print("No contacts found.")
        else:
            contact = found_contacts[0]
            self.contacts.remove(contact)
            print("Contact deleted successfully.")

    def display_contact(self, contact):
        print(f"Name: {contact.name}")
        print(f"Phone: {contact.phone}")
        print(f"Email: {contact.email}")
        print(f"Address: {contact.address}")

def main():
    manager = ContactManager()
    
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            manager.add_contact(name, phone, email, address)
        elif choice == '2':
            manager.view_contacts()
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            manager.search_contact(search_term)
        elif choice == '4':
            search_term = input("Enter name or phone number to update: ")
            manager.update_contact(search_term)
        elif choice == '5':
            search_term = input("Enter name or phone number to delete: ")
            manager.delete_contact(search_term)
        elif choice == '6':
            print("Exiting Contact Manager.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if _name_ == "_main_":
    main()
