"""
Welcome to Receipt Buddy! Exit by typing: quit
Enter an amount: 25
Enter an amount: 50
Enter an amount: quit
The total is 75 kr. Welcome back!

"""
total = 0.0  # use float for decimals

print("Welcome to Receipt Buddy! Exit by typing: quit")

while True:
    user_input = input("Enter an amount: ")
    if user_input.lower() == "quit":
        break
    if user_input.strip() == "":
        print("Please enter an amount or 'quit' to exit.")
        continue
    try:
        amount = float(user_input.replace(",", "."))
        total += amount
    except ValueError:
        print("No digits detected! Please enter a valid amount.")
print(f"The total is {total}. Welcome back!")
