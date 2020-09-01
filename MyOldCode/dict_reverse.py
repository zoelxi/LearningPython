def dict_reverse(inputDict):
    outputDict = {}
    for (k,v) in inputDict.items():
        outputDict[v] = k
    return outputDict

testDict = {'adam':80,'betty':60,'charles':50}
reversedDict = dict_reverse(testDict)
print(reversedDict)
