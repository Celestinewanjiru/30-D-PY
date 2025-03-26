import random

# Function for the number guessing game
def number_guessing_game():
    # Randomly choose a number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    # max_attempts = 3 if trials are limited to 3 
    guessed = False
    
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it!")

    # Loop until the user guesses the correct number
    while not guessed:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the correct number {number_to_guess} in {attempts} attempts.")
                guessed = True

        except ValueError:
            print("Please enter a valid number!")
''' If the user reaches the max attempts, the game ends
        if attempts == max_attempts and not guessed:
            print(f"Sorry, you've reached the maximum attempts of {max_attempts}. The number was {number_to_guess}.") '''


# Call the game function
if __name__ == "__main__":
    number_guessing_game()
