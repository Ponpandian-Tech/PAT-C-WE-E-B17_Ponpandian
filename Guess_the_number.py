import random

print("Welcome to the Guess the Number Game!")

# Computer selects a random number between 1 and 100
secret_number = random.randint(1 , 100)

while True:
    # Player enters a guess
    user_guess = int(input("Enter your guess (1–100): "))

    # Check conditions
    if user_guess == secret_number:
        print("congratulations!!! You have guessed right!!!")
    else:
        print(f"Try again, correct number was {secret_number}")
