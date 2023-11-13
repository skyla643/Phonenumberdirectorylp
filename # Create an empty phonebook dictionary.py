# Create an empty phonebook dictionary
phonebook = {}

# Function to add a phone number to the phonebook
def add_phone_number(name, phone_number):
    phonebook[name] = phone_number
    print("Phone number added successfully.")

# Function to retrieve phone numbers by name
def get_phone_number(name):
    if name in phonebook:
        print(f"Name: {name}, Phone Number: {phonebook[name]}")
    else:
        print(f"{name} not found in the phonebook.")

# Main program loop
while True:
    print("Phonebook Database")
    print("1. Add a Phone Number")
    print("2. Search for a Phone Number")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter the name: ")
        phone_number = input("Enter the phone number: ")
        add_phone_number(name, phone_number)
    elif choice == '2':
        name = input("Enter the name to search for: ")
        get_phone_number(name)
    elif choice == '3':
        break
