def permute(inputList):
    if len(inputList) == 0:
        return [[]]
    outputList = []
    for i in range(len(inputList)):
        first = inputList.pop(i)
        perms = permute(inputList)
        for perm in perms:
            perm.insert(0,first)
        outputList.extend(perms)
        inputList.insert(i,first)
    return outputList

print(permute([1,2]))
# should print [[1,2], [2,1]] in some order
print(permute([1,2,3]))
    
    
    
