import os

FILENAME = "contacts.txt"

# -------------------------
# Function: Add Contact
# -------------------------
def add_contact():
    try:
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")
        email = input("Enter Email: ")

        with open(FILENAME, "a") as file:
            file.write(f"{name},{phone},{email}\n")

        print("✅ Contact added successfully!\n")

    except Exception as e:
        print("❌ Error while adding contact:", e)


# -------------------------
# Function: View All Contacts
# -------------------------
def view_contacts():
    try:
        with open(FILENAME, "r") as file:
            contacts = file.readlines()

        if not contacts:
            print("📂 No contacts found.\n")
            return

        print("\n📒 Contact List:")
        for line in contacts:
            name, phone, email = line.strip().split(",")
            print(f"Name: {name}, Phone: {phone}, Email: {email}")
        print()

    except FileNotFoundError:
        print("⚠️ Contact file not found! Add a contact first.\n")
    except Exception as e:
        print("❌ Error while reading contacts:", e)


# -------------------------
# Function: Search Contact
# -------------------------
def search_contact():
    try:
        keyword = input("Enter name or phone to search: ").lower()

        with open(FILENAME, "r") as file:
            contacts = file.readlines()

        found = False
        for line in contacts:
            name, phone, email = line.strip().split(",")
            if keyword in name.lower() or keyword in phone:
                print(f"✅ Found: Name: {name}, Phone: {phone}, Email: {email}")
                found = True

        if not found:
            print("🔍 No matching contact found.\n")

    except FileNotFoundError:
        print("⚠️ Contact file not found! Add a contact first.\n")
    except Exception as e:
        print("❌ Error while searching contact:", e)


# -------------------------
# Main Program Loop
# -------------------------
def main():
    while True:
        print("\n====== CONTACT BOOK ======")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("⚠️ Invalid choice, please try again.\n")


if __name__ == "__main__":
    main()
