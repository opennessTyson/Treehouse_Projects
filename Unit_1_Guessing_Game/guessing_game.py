import random

def start_game():
    random_number = random.randrange(1,11)
    attempts = 1
    guess = 0
    name = input("Hello Friend. Welcome to Guessing Game, what should we call you?:  ")
    while  guess !=  random_number:
        try:
            guess = int(input("{}, guess a number between 0-10.  ".format(name)))
            if guess > 10 or guess < 1:
                raise ValueError("Please enter a number between 1-10")
        except ValueError as err:
            print("We ran into an issue {}. Please try again".format(err))
        else:
            if guess < random_number:
                print("It's higher")
                attempts += 1
            elif guess >random_number:
                print("It's lower")
                attempts += 1
            elif guess == random_number:                 
                print("Got it")
                print("You are too good. Game over in {} attempts. ".format(attempts))
    while True:
        if guess == random_number:
                play_again = input("Would you like to play again? Y/N?")
                if play_again.lower() == "y":
                    start_game()
                    continue
                elif play_again.lower() == "n":
                    break
                else:
                    print("Enter either Y/N...")
start_game()