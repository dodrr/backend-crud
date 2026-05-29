# Watch Store Backend
from users import (
    add_user,
    get_user,
    update_user,
    delete_user,
    get_all_users,
    count_users
)

while True:
    print("\n--- USER SYSTEM ---")
    print("1. Add user")
    print("2. Get user")
    print("3. Update user")
    print("4. Delete user")
    print("5. Show all users")
    print("6. Count users")
    print("0. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        age = int(input("Age: "))
        add_user(name, age)

    elif choice == "2":
        name = input("name:")
        print(get_user(name))

    elif choice == "3":
        name = input("Name:")
        age = int(input("new age:"))
        update_user(name, age)

    elif choice == "4":
        name = input("Name:")
        delete_user(name)

    elif choice == "5":
        print(get_all_users())

    elif choice == "6":
        print(count_users())

    elif choice == "0":
        break

    else:
        print("Invalid choice")



