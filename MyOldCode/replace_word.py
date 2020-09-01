def replace_word(filename,oldWord,newWord):
    f = open(filename, 'r')
    string = f.read()
    f.close()
    newList = []
    oldList = string.split()
    for word in oldList:
        if word == oldWord:
            newList.append(newWord)
        else:
            newList.append(word)
    glue = ' '
    newString = glue.join(newList)
    print(newString)

replace_word('dorothy.txt','Toto','Gizmo')
    
            
