#This code should calculate how much money is left after buying a ticket.
# The remaining money should then be shared with a friend.
# The code hasn’t been tested. Are there any errors in the code?

"""
x = 100  # biljettpris
y = 200  # pengar på fickan
print("Det blir " + (y - x) " kronor över.")
z = y - x / 2
print("Varje person får " + z)
"""

ticket_price = 100
pocket_money = 200
print("There will be " + str(pocket_money - ticket_price) +  " kron left.")
money_left= pocket_money - ticket_price /2
print("Each person gets " + str(money_left))
