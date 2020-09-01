import random

computerNumber = random.randrange(101) # computer randomly selects an integer between 0 to 100, inclusive
print("Hello user! I'm thinking of a number between 0 and 100. Can you guess what my number is?")
count = 0 
while True: # play until the user guesses the integer
    guess = int(input("Enter your guess: "))
    count += 1 # counts the number of guesses
    # checks if guess is lower than the integer and tells user
    if guess < computerNumber:
        print("Sorry, " + str(guess) + " is too low. Please try again!")
    # checks if guess is higher than the integer and tells user
    elif guess > computerNumber:
        print("Sorry, " + str(guess) + " is too high. Please try again!")
    # checks if user wins and tells user
    elif guess == computerNumber:
        print("Yay! You guessed my number, " + str(guess) + ".")
        print("It took you " + str(count) + " guesses. Play again soon!") # tells user the number of guesses
        break
