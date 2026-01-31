"""
Bygg ett program där användaren kan lägga till saker till en todo-lista.
Tips: använd en loop, input och en variabel för listan.
Exempel:

** Todo list extravaganza **
1. Se innehållet i din lista
2. Lägga till nya punkter i din lista
Välj ett alternativ: 1
Din lista är tom
.
Välj ett alternativ: 2
Skriv in en ny sak du måste komma ihåg att göra: mata guldfisken
Ok, lade till "mata guldfisken" i listan.
.
Välj ett alternativ: 1
+ Mata guldfisken
.
"""
# Version 1 - Basic Todo List

todo_list = []

print("** Todo List Extravaganza **")

while True:
    print("\n1. View your list")
    print("2. Add a new item")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        if not todo_list:
            print("Your list is empty.")
        else:
            print("Your todo list:")
            for idx, item in enumerate(todo_list, 1):
                print(f"+ {item}")

    elif choice == "2":
        new_item = input("Enter a new item to remember: ")
        todo_list.append(new_item)
        print(f'Ok, added "{new_item}" to the list.')

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose 1, 2, or 3.")
