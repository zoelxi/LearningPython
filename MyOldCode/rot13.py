def rot13(string):
    encodedString = ''
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    for character in string:
        if character in alphabet:
            number = ord(character)
            if number < 78 or 96 < number < 110:
                newNumber = number + 13
            else:
                newNumber = number - 13
            newCharacter = chr(newNumber)        
            encodedString += newCharacter
        else:
            encodedString += character
    return encodedString

print(rot13('Hello, World!!'))


