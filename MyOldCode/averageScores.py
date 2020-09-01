inFile = open('grades.txt','r')
grades = {}
count = 0
for line in inFile:
    gradeList = line.split()
    if gradeList[0] in grades:
        grades[(gradeList[0])] += int(gradeList[1])
    else:
        grades[(gradeList[0])] = int(gradeList[1])
    count += 1
inFile.close()
for (k,v) in grades.items():
    v = int(v)/count
    grades[k] = v
print(grades)
