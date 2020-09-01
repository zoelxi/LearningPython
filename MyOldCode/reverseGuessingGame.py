import random
number = int(input('Please select a number between 0 and 1000, inclusive: '))
if number < 0 or number > 1000:
    number = int(input('Your number is not in the given range. Please select a number between 0 and 1000, inclusive: '))
guess = random.randrange(1001)
guessCount = 1
lowerLimit = -1
upperLimit = 1001
while True:
    print('I guess ' + str(guess))
    response = input('Is this high, low, or correct? ')
    if response not in ['high','low','correct']:
        response = input('Your response is invalid. Please try again. Is this high, low, or correct? ')
    if response == 'high':
        upperLimit = guess
        guess = random.randrange(lowerLimit+1,upperLimit)
        guessCount += 1
    elif response == 'low':
        lowerLimit = guess
        guess = random.randrange(lowerLimit+1,upperLimit)
        guessCount += 1
    elif response == 'correct':
        print('I knew it! It took me ' + str(guessCount) + ' guesses.')
        break
    
