import random

class Die:
    '''Die class'''

    def __init__(self,sidesParam=6):
        '''Die([sidesParam])
        creates a new Die object
        int sidesParam is the number of sides
        (default is 6)
        -or- sidesParam is a list/tuple of sides'''
        # if an integer, create a die with sides
        #  from 1 to sides
        if isinstance(sidesParam,int):
            sidesParam = range(1,sidesParam+1)
        self.sides = list(sidesParam)
        self.numSides = len(self.sides)
        # roll the die to get a random side on top to start
        self.roll()

    def __str__(self):
        '''str(Die) -> str
        string representation of Die'''
        return 'A ' + str(self.numSides) + '-sided die with ' + \
               str(self.get_top()) + ' on top'

    def roll(self):
        '''Die.roll()
        rolls the die'''
        # pick a random side and put it on top
        self.top = random.choice(self.sides)

    def get_top(self):
        '''Die.get_top() -> object
        returns top of Die'''
        return self.top

    def set_top(self,value):
        '''Die.set_top(value)
        sets the top of the Die to value
        Does nothing if value is illegal'''
        if value in self.sides:
            self.top = value

    def flip(self):
        index = self.sides.index(self.top)
        self.sides.reverse()
        self.top = self.sides[index]

def europadice():
    diceList = []
    sides = [1,2,3,4,'W']
    dice = Die(sides)
    for d in range(10):
        dice.roll()
        top = dice.get_top()
        diceList.append(top) 
    greatestNum = 0
    for side in sides[:4]:
        count = diceList.count(side)
        if count > greatestNum:
            greatestNum = count
            mostCommonSide = side
    diceString = ''
    for d in diceList:
        diceString += str(d) + ' '
    print(diceString)
    print("We're going for all " + str(mostCommonSide) + 's')
    unwantedSides = [s for s in diceList if s not in (mostCommonSide,'W')]
    for s in unwantedSides:
        diceList.remove(s)
    print(diceList)
    reroll = 1
    while unwantedSides != [] and reroll <= 3:
        input('Reroll #' + str(reroll) + '. Press enter to reroll. ')
        length = len(unwantedSides)
        unwantedSides = []
        for d in range(length):
            dice.roll()
            top = dice.get_top()
            unwantedSides.append(top)
        for t in unwantedSides:
            if t in (mostCommonSide,'W'):
                unwantedSides.remove(t)
                diceList.append(t)
        diceString = ''
        for dice in diceList:
            diceString += str(dice) + ' '
        print(diceString)
        reroll += 1
    if unwantedSides == []:
        print('Yay, you win!')
    else:
        print('Sorry, only got ' + str(10-len(unwantedSides)))
        

        
        
        
