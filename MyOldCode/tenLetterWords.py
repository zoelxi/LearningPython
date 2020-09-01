f = open('wordlist.txt','r')
wordString = f.read()
wordList = wordString.split()
f.close()
count = 0
for word in wordList:
    if len(word) == 10:
        count +=1
print(count)
