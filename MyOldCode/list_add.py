def list_add(list1,list2):
    newList = []
    if len(list1) == len(list2):
        for i in range(len(list1)):
            newElement = list1[i] + list2[i]
            newList.append(newElement)
    return newList


            
