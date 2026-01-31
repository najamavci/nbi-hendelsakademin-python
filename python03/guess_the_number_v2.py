import random

secret = random.randint(1, 100)
guesses = 0

print("Welcome to Guess the Number!")
print("I am thinking of a number between 1 and 100. Can you guess it?")

while True:
    guess_input = input("Your guess: ")

    # Validate input
    if not guess_input.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess_input)
    guesses += 1

    if guess == secret:
        print(f"Correct!! You guessed it in {guesses} tries.")
        break
    elif abs(guess - secret) <= 5:  # within 5 → getting close
        print("You're getting close!")
        if guess < secret:
            print("But it’s still too low.")
        else:
            print("But it’s still too high.")
    else:
        if guess < secret:
            print("No, it’s too low!")
        else:
            print("No, it’s too high!")
