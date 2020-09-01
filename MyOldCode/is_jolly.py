def is_jolly(inList):
    jollyList = []
    for i in range(len(inList)-1):
       x = inList[i+1]-inList[i]
       jollyList.append(abs(x))
    jollyList.sort()
    for i in range(len(jollyList)-1):
        if jollyList[i+1]-jollyList[i] != 1:
            return False
    return True

print(is_jolly([6,9,7,8]))  
print(is_jolly([1,4,3,2]))
    
