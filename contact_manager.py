# contact_manager.py


"""A simple program for adding, finding, and deleting contacts."""


contacts = {}


class DuplicateContactError(Exception):
    """Raised when a contact already exists."""


def add_contact(name, phone):
    """Add a new contact and prevent duplicate names."""
    if name in contacts:
        raise DuplicateContactError(f"{name} already exists.")

    contacts[name] = phone
    print(f"Added {name} to contacts.")


def find_contact(name):
    """Find a contact and display their phone number."""
    try:
        phone = contacts[name]
        print(f"{name}: {phone}")
        return phone
    except KeyError:
        # Handle contacts that don't exist.
        print("Contact not found.")
        return None


def delete_contact(name):
    """Delete a contact from the contact list."""
    try:
        del contacts[name]
        print(f"Deleted {name}.")
    except KeyError:
        print("Contact not found.")


def main():
    """Display the menu and handle the user's choices."""
    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. Find Contact")
        print("3. Delete Contact")
        print("4. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 4.")
            continue
        
        if choice == 1:
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            try:
                add_contact(name, phone)
            except DuplicateContactError as error:
                print(error)
        elif choice == 2:
            name = input("Enter name to find: ")
            find_contact(name)
        elif choice == 3:
            name = input("Enter name to delete: ")
            delete_contact(name)
        elif choice == 4:
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()