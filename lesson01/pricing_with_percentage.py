#2a. Now it’s time to buy winter clothes.
# You see a nice jacket that costs 2000 kronor. The jacket is on sale and costs 75% of the original price.
# Write a program that calculates how much you need to pay. Use the variable:
# sale_percent = 75.0

sale_percent = 75.0
jacket_price= 2000
final_price = jacket_price * sale_percent / 100
print("The final price of the jacket is", int(final_price))

#2b. Modify the program so that the user can enter a percentage.
#Test it by choosing a percentage and calculating what the program should return before running it.
# For example, 10%, which is 200 kr. Then the jacket should cost: 2000 - 200 == 1800 kr

sale_percentage= int(input("Please, enter the sale percentage "))
actual_price= 3500
print("The actual price of the jacket is", int(actual_price))
discount_amount = actual_price * sale_percentage / 100
print("The discount amount is", int(discount_amount))
item_final_price = actual_price - discount_amount
print("The item costs", int(item_final_price), "Swedish kron")