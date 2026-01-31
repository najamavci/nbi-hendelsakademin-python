# Version 3 - Archive Completed Items

todo_list = []
done_list = []

print("** Todo List Extravaganza **")

while True:
    print("\n1. View your list")
    print("2. Add a new item")
    print("3. Mark an item as done")
    print("4. View done items")
    print("5. Restore an item from done list")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        if not todo_list:
            print("Your todo list is empty.")
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
                done_list.append(done_item)
                print(f'Ok, moved "{done_item}" to done list.')
            else:
                print("Invalid number.")

    elif choice == "4":
        if not done_list:
            print("No completed items yet.")
        else:
            print("Completed items:")
            for idx, item in enumerate(done_list, 1):
                print(f"{idx}. {item}")

    elif choice == "5":
        if not done_list:
            print("No items to restore.")
        else:
            for idx, item in enumerate(done_list, 1):
                print(f"{idx}. {item}")
            restore_index = input("Enter the number of the item to restore: ")
            if restore_index.isdigit() and 1 <= int(restore_index) <= len(done_list):
                restored_item = done_list.pop(int(restore_index) - 1)
                todo_list.append(restored_item)
                print(f'Ok, moved "{restored_item}" back to todo list.')
            else:
                print("Invalid number.")

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose a number from the menu.")
