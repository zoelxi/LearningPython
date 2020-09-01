def translate():
    '''translate() -> None
    Prompts user to enter dictionary files and input and output files
    Changes words in input file according to the dictionary file
    Write translation in output file'''
    dictFileName = input('Enter name of dictionary: ')
    textFileName = input('Enter name of text file to translate: ')
    outputFileName = input('Enter name of output file: ' )

    dictFile = open(dictFileName,'r')
    dictionary = {}
    for line in dictFile:
        line = line.lower()
        for char in '|':
            line = line.replace(char,' ')
        dictList = line.split()
        dictionary[dictList[0]] = dictList[1]
    dictFile.close()

    textFile = open(textFileName,'r')
    outputFile = open(outputFileName,'w')
    for line in textFile:
        line = line.lower()
        textList = line.split()
        for word in textList:
            if word in dictionary:
                outputFile.write(dictionary[word])
            else:
                outputFile.write(word)
            outputFile.write(' ')
        outputFile.write('\n')
    textFile.close()
    outputFile.close()
            
print(translate())
