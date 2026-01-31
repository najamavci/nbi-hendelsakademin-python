"""
Version 2: programmet ska fråga hur många man är, och tala om hur mycket varje person i sällskapet ska betala.
Hur många är ni? 3
Det blir 75 kr totalt, alltså 25.0 kr per person. Välkommen åter!
"""

total = 0.0

print("Welcome to Receipt Buddy! Exit by typing: quit")

while True:
    user_input = input("Enter an amount: ")
    if user_input.lower() == "quit": #if user input equals quit
        break
    if user_input.strip() == "": # if user input equals nothing
        print("Please enter an amount or 'quit' to exit.")
        continue
    try:
        amount = float(user_input.replace(",", ".")) #if user input equals a number like 34,5
        total += amount
    except ValueError:
        print("No digits detected! Please enter a valid amount.")
print(f"The total is {total}. Welcome back!")

while True:
    num_people = input("How many people are there? ")
    if num_people.isdigit() and int(num_people) > 0:
        num_people = int(num_people)
        break
    else:
        print("Please enter a valid positive number of people.")

amount_per_person = total / num_people

print(f"The total is {total} currency units, so each person should pay {amount_per_person:.2f}. Welcome back!")