def anagrams(inputString):
    if len(inputString) == 0:
        return ['']
    outputList = []
    for i in range(len(inputString)):
        first = inputString[i]
        anagramEndings = anagrams(inputString[:i] + inputString[i+1:])
        for anagramEnding in anagramEndings:
            anagram = inputString[i] + anagramEnding
            outputList.append(anagram)
    return outputList

def jumble_solve(inputString):
    wordFile = open('wordlist.txt','r')
    wordString = wordFile.read()
    wordList = wordString.split()
    wordFile.close()
    anagramsList = anagrams(inputString)
    validAnagrams = []
    for anagram in anagramsList:
        for word in wordList:
            if word == anagram or word.upper() == anagram:
                validAnagrams.append(anagram)
    return validAnagrams

print(jumble_solve('CHWAT'))
print(jumble_solve('RAROM'))
print(jumble_solve('CEPLIN'))
print(jumble_solve('YAFLIM'))
        
        
