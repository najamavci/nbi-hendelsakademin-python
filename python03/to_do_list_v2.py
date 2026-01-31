# Version 2 - Add "Mark as Done"

todo_list = []

print("** Todo List Extravaganza **")

while True:
    print("\n1. View your list")
    print("2. Add a new item")
    print("3. Mark an item as done")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        if not todo_list:
            print("Your list is empty.")
        else:
            print("Your todo list:")
            for idx, item in enumerate(todo_list, 1):
                print(f"{idx}. {item}")

    elif choice == "2":
        new_item = input("Enter a new item to remember: ")
        todo_list.append(new_item)
        print(f'Ok, added "{new_item}" to the list.')

    elif choice == "3":
        if not todo_list:
            print("Your list is empty, nothing to mark as done.")
        else:
            for idx, item in enumerate(todo_list, 1):
                print(f"{idx}. {item}")
            done_index = input("Enter the number of the item you finished: ")
            if done_index.isdigit() and 1 <= int(done_index) <= len(todo_list):
                done_item = todo_list.pop(int(done_index) - 1)
                print(f'Ok, removed "{done_item}" from the list.')
            else:
                print("Invalid number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose 1, 2, 3, or 4.")
