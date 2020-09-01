import random

header = 'roll\tnumber\n----\t------'
print(header)

rollList = []
table = ''
for i in range(1001):
    dice1 = random.randrange(1,7)
    dice2 = random.randrange(1,7)
    rollList.append(dice1+dice2)
for j in range(2,13):
    numberOfRolls = rollList.count(j)
    table += str(j)
    if j < 10:
        table += ' '
    table += '  \t' + str(numberOfRolls) + '\n'
print(table)
        
    




    
