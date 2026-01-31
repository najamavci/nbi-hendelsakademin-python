"""
5 Gissa talet
Gör ett spel som slumpar ett hemligt tal mellan 1 och 100. Sedan ska man försöka gissa det. Om man gissar för lågt eller för högt ska spelet tala om det. Efter att man har gissat rätt ska spelet skriva ut antalet gissningar.

# Slumpa ett hemligt tal
secret = random.randint(1, 100)

Exempel:
Välkommen till gissa talet! Jag tänker på ett tal mellan 1 och 100. Kan du gissa vilket det är?
Gissa: 40
Nej, det är för lågt!
Gissa: 55
Nej, det är för högt!
Gissa: 51
Det är rätt!! Du gjorde det på 3 gissningar.

Version 2: skriv ut om man är nära ifall man gissar högst 5 ifrån det rätta svaret.
"Nu börjar det brännas!"

"""

import random

# Randomly select a secret number between 1 and 100
secret = random.randint(1, 100)
guesses = 0

print("Welcome to Guess the Number!")
print("I am thinking of a number between 1 and 100. Can you guess it?")

while True:
    guess_input = input("Your guess: ")

    # Check if input is a number
    if not guess_input.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess_input)
    guesses += 1

    if guess < secret:
        print("No, it’s too low!")
    elif guess > secret:
        print("No, it’s too high!")
    else:
        print(f"Correct!! You guessed it in {guesses} tries.")
        break
