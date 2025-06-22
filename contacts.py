n = int(input("How many contacts you want to add: "))
for i in range(n):
    k = input("Enter name: ").lower()
    while True:
        v = input("Enter number: ")
        if v.isdigit() and len(v) == 10 and v[0] in '9876':
            phone = int(v)
            contact[k] = phone
            break
        else:
            print("Invalid number. Please enter a valid Indian mobile number.")

print("Your contacts are:", contact)

while True:
    print("\n__Instructions__")
    print("1) Add new contact")
    print("2) Search contact")
    print("3) View all contacts")
    print("4) Exit")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        x = input("Enter name: ").lower()
        while True:
            y = input("Enter number: ")
            if y.isdigit() and len(y) == 10 and y[0] in '9876':
                phone = int(y)
                contact[x] = phone
                print("Contact added successfully.")
                break
            else:
                print("Invalid number. Please enter a valid Indian mobile number.")

    elif choice == 2:
        search_name = input("Enter name to search: ").lower()
        if search_name in contact:
            print(f"{search_name} - {contact[search_name]}")
        else:
            print("Contact not found.")

    elif choice == 3:
        print("All Contacts:")
        for name, number in contact.items():
            print(f"{name} - {number}")

    elif choice == 4:
        print("Exiting the contact book...")
        break

    else:
        print("Invalid choice. Please enter 1 to 4.")
