f = open('wordlist.txt','r')
wordString = f.read()
wordList = wordString.split()
f.close()
values = {'A':1,'B':3,'C':3,'D':2,'E':1,'F':4,'G':2,'H':4,'I':1,
          'J':8,'K':5,'L':1,'M':3,'N':1,'O':1,'P':3,'Q':10,'R':1,
          'S':1,'T':1,'U':1,'V':4,'W':4,'X':8,'Y':4,'Z':10}
highestScore = 0
for word in wordList:
    wordScore = 0
    word = word.upper()
    if 'Z' in word:
        continue
    if len(word) != 7:
        continue
    for letter in word:
        wordScore += values[letter]
    if wordScore > highestScore:
        highestScore = wordScore
        bestWord = word

print(bestWord)

