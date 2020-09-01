def letter_count(inputString):
    letterCounts = {}
    inputString = inputString.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter in inputString:
        if letter in alphabet:
            if letter in letterCounts:
                letterCounts[letter] += 1
            else:
                letterCounts[letter] = 1
    letterCounts = list(letterCounts.items())
    letterCounts.sort()
    return letterCounts

print(letter_count("I like learning Python at Art of Problem Solving!"))
