total = 0.0  # allow decimals

print("Welcome to Receipt Buddy! Exit by typing: quit")

# Step 1: Enter amounts
while True:
    user_input = input("Enter an amount: ")

    # Exit condition
    if user_input.lower() == "quit":
        break

    # Empty input
    if user_input.strip() == "":
        print("Please enter an amount or 'quit' to exit.")
        continue

    # Try converting to a number
    try:
        # Replace comma with dot for decimals
        amount = float(user_input.replace(",", "."))
        total += amount
    except ValueError:
        print("No digits detected! Please enter a valid amount.")

# Step 2: Ask how many people
while True:
    num_people_input = input("How many people are there? ")
    if num_people_input.isdigit() and int(num_people_input) > 0:
        num_people = int(num_people_input)
        break
    else:
        print("Please enter a valid positive number of people.")

# Step 3: Ask tip percentage (default 10%)
tip_input = input("What percentage tip would you like to add? (Press Enter for 10%) ")

try:
    if tip_input.strip() == "":  # empty input → default 10%
        tip_percent = 10.0
    else:
        tip_percent = float(tip_input.replace(",", "."))
except ValueError:
    print("Invalid tip input. Using default 10%.")
    tip_percent = 10.0

# Step 4: Calculate tip and total per person
total_with_tip = total * (1 + tip_percent / 100)
amount_per_person = total_with_tip / num_people

# Step 5: Print final results
print(f"The total is {total:.2f} currency units.")
print(f"With {tip_percent:.0f}% tip, the total is {total_with_tip:.2f} currency units.")
print(f"Each person should pay {amount_per_person:.2f}. Welcome back!")
