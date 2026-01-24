level1 = 100
level2 = 300
discount = 0

price = float(input("Welcome, please enter your price: "))

if level1 <= price < level2:
    print("Congratulations! You are eligible for level 1 and you get 10% discount.")
    discount = 10
elif price >= level2:
    print("Congratulations! You are eligible for level 2 and you get 25% discount.")
    discount = 25
else:
    print("Sorry to inform you, but you are not eligible for a discount.")

final_price = price * (100 - discount) / 100
print("Your price after the discount is:", final_price)
