f = open('africa.txt','r')
text = f.read()
f.close()
eightLetterWords = []
wordList = text.split()
for word in wordList:
    if len(word) == 8:
        eightLetterWords.append(word)
print(len(eightLetterWords))
        
