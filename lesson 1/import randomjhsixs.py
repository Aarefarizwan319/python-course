import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    secret_number = random.randint(1, 20)
    while True:
        try:
            guess = int(input("Guess a number between 1 and 20: "))
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the right number {secret_number}")
                break
        except ValueError:
            print("Please enter a valid number.")

number_guessing_game()
