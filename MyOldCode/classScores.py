inFile = open('classgrades.txt','r')
outFile = open('classscores.txt','w')
for line in inFile:
    line = line.strip('\n')
    studentGrades = line.split()
    scoreSum = 0
    for i in range(1,len(studentGrades)):
        scoreSum += int(studentGrades[i])
        studentScore = scoreSum // (len(studentGrades) - 1)
    outFile.write(studentGrades[0] + ' ' + str(studentScore) + '\n')
inFile.close()
outFile.close()
    
    
    
