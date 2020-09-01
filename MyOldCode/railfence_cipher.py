def encipher_fence(plaintext,numRails):
    '''encipher_fence(plaintext,numRails) -> str
    encodes plaintext using the railfence cipher
    numRails is the number of rails'''
    railDic = {}
    for num in range(numRails):
        index = num # start with character in position num
        rail = ''
        # form rail num
        while index < len(plaintext):
            # take every nth character following
            rail += plaintext[index] 
            index += numRails
        railDic[num] = rail # add each rail to a rail dictionary
    ciphertext = ''
    # concatenate rails in reverse order to form ciphered text
    num = numRails - 1 
    while num >= 0:
        ciphertext += railDic[num]
        num -= 1
    return ciphertext

def decipher_fence(ciphertext,numRails):
    '''decipher_fence(ciphertext,numRails) -> str
    returns decoding of ciphertext using railfence cipher
    with numRails rails'''
    railDic = {}
    minRailLen = len(ciphertext) // numRails
    rem = len(ciphertext) % numRails
    end = len(ciphertext) # end of rail 0
    # move beginning of rail one character earlier if remainder is positive
    for num in range(numRails):
        if rem > 0:
            delta = 1
        else:
            delta = 0
        beg = end - minRailLen - delta
        railDic[num] = ciphertext[beg:end] # add each rail to a rail dictionary
        rem -= 1
        end = beg
    plaintext = ''
    index = 0
    while True:
        # add character from same index of each rail to plain text if index is inside allowed range of rail
        for rail in railDic.values():
            if index < len(rail):
                plaintext += rail[index]
        # leave loop if index is outside allowed range of longest rail
        if index > minRailLen:
            break
        # move to next index
        else:
            index += 1
    return plaintext

def decode_text(ciphertext,wordfilename):
    '''decode_text(ciphertext,wordfilename) -> str
    attempts to decode ciphertext using railfence cipher
    wordfilename is a file with a list of valid words'''
    wordFile = open(wordfilename,'r')
    wordString = wordFile.read()
    wordList = wordString.split() # create list of English words
    wordFile.close()
    textDic = {}
    greatestWordCount = 0
    for numRails in range(2,11):
        text = decipher_fence(ciphertext,numRails)
        textDic[numRails] = text # add decoded texts using each number of rails from 2 to 11, inclusive, to dictionary
    punct = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    # remove punctuation from each decoded text in dictionary
    for text in textDic.values():
        textWithoutPunct = ''
        for letter in text:
            if letter not in punct:
                textWithoutPunct += letter
        textWords = textWithoutPunct.split() # split text without punctuation into list of words
        wordCount = 0
        # count number of words in both decoded text word list and English word list
        for textWord in textWords:
            for word in wordList:
                if word == textWord:
                    wordCount += 1
        # find decoded text with most English words in it
        if wordCount > greatestWordCount:
            greatestWordCount = wordCount
            plaintext = text
    return plaintext 

# test cases

# enciphering
print(encipher_fence("abcdefghi", 3))
# should print: cfibehadg
print(encipher_fence("This is a test.", 2))
# should print: hsi  etTi sats.
print(encipher_fence("This is a test.", 3))
# should print: iiae.h  ttTss s
print(encipher_fence("Happy birthday to you!", 4))
# should print: pidtopbh ya ty !Hyraou

# deciphering
print(decipher_fence("hsi  etTi sats.",2))
# should print: This is a test.
print(decipher_fence("iiae.h  ttTss s",3))
# should print: This is a test.
print(decipher_fence("pidtopbh ya ty !Hyraou",4))
# should print: Happy birthday to you!

# decoding
print(decode_text(" cr  pvtl eibnxmo  yghu wou rezotqkofjsehad", 'wordlist.txt'))
# should print: the quick brown fox jumps over the lazy dog
print(decode_text("unt S.frynPs aPiosse  Aa'lgn lt noncIniha ", 'wordlist.txt'))
# should print... we'll let you find out!
