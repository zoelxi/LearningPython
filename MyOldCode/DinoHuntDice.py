# Python Class 2256
# Lesson 6 Problem 5
# Author: zxi (179194)

import random

### Die class that we previously wrote ###

class Die:
    '''Die class'''

    def __init__(self,sides=6):
        '''Die(sides)
        creates a new Die object
        int sides is the number of sides
        (default is 6)
        -or- sides is a list/tuple of sides'''
        # if an integer, create a die with sides
        #  from 1 to sides
        if isinstance(sides,int):
            self.numSides = sides
            self.sides = list(range(1,sides+1))
        else:  # use the list/tuple provided 
            self.numSides = len(sides)
            self.sides = list(sides)
        # roll the die to get a random side on top to start
        self.roll()

    def __str__(self):
        '''str(Die) -> str
        string representation of Die'''
        return 'A '+str(self.numSides)+'-sided die with '+\
               str(self.get_top())+' on top'

    def roll(self):
        '''Die.roll()
        rolls the die'''
        # pick a random side and put it on top
        self.top = self.sides[random.randrange(self.numSides)]

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

### end Die class ###

class DinoDie(Die):
    '''implements one die for Dino Hunt'''

    def __init__(self,color):
        '''DinoDie(color)
        creates a new DinoDie object
        str color is color of die'''
        self.numSides = 6 
        # different colors correspond to dice with different sides
        self.color = color
        if self.color == 'green':
            self.sides = ['dino','dino','dino','leaf','leaf','foot']
        elif self.color == 'yellow':
            self.sides = ['dino','dino','leaf','leaf','foot','foot']
        elif self.color == 'red':
            self.sides = ['dino','leaf','leaf','foot','foot','foot']
        self.roll() # roll the die to get a random side on top to start

    def __str__(self):
        '''str(DinoDie) -> str
        str representation of DinoDie'''
        return 'A ' + self.color + ' Dino die with a ' + self.get_top() + ' on top.'

    def get_color(self):
        '''DinoDie.get_color() -> str
        returns color of die'''
        return self.color

class DinoPlayer:
    '''implements a player of Dino Hunt'''

    def __init__(self,name):
        '''DinoPlayer(name)
        creates a new DinoPlayer object
        str name is name of player'''
        self.name = name
        self.totalPoints = 0
        self.turnPoints = 0
        self.stomp = 0 # num feet accumulated during one turn
        self.hand = [] # randomly selected dice
        self.dicePile = [] # unrolled dice
        self.fill_pile() # fill dice pile with 13 colored six-sided dice

    def __str__(self):
        '''str(DinoPlayer) -> str
        str representation of DinoPlayer'''
        return self.name + ' has ' + str(self.totalPoints) + ' points.'

    def get_points(self):
        '''DinoPlayer.get_points() -> int
        returns total num of points player has accumulated'''
        return self.totalPoints

    def find_num_color(self):
        '''DinoPlayer.find_num_color() - > str
        returns number of dice of each color in player's dice pile'''
        # create lists of dice of each color
        greenDice = [dice for dice in self.dicePile if dice.get_color() == 'green']
        yellowDice = [dice for dice in self.dicePile if dice.get_color() == 'yellow']
        redDice = [dice for dice in self.dicePile if dice.get_color() == 'red']
        return str(len(greenDice)) + ' green, ' + str(len(yellowDice)) + ' yellow, ' + str(len(redDice)) + ' red'

    def fill_pile(self):
        '''DinoPlayer.fill_pile()
        empties and fills player's dice pile with 13 colored six-sided dice'''
        self.dicePile = []
        # fill pile with 6 green, 4 yellow, and 3 red dice
        for g in range(6):
            self.dicePile.append(DinoDie('green'))
        for y in range(4):
            self.dicePile.append(DinoDie('yellow'))
        for r in range(3):
            self.dicePile.append(DinoDie('red'))
        random.shuffle(self.dicePile) # shuffle the pile

    def reset(self):
        '''DinoPlayer.reset()
        resets turn points and num feet accumulated during turn to 0 and fills pile'''
        self.turnPoints = 0
        self.stomp = 0
        self.fill_pile()

    def take_turn(self):
        '''DinoPlayer.take_turn()
        takes player's turn in game'''
        # print player info
        print(self.name + ", it's your turn!")
        print('You have ' + str(len(self.dicePile)) + ' dice remaining.')
        print(self.find_num_color())
        while True:
            input('Press enter to select dice and roll. ')
            # end turn if no dice left in dice pile to roll
            if len(self.dicePile) == 0:
                print('You have no dice left to roll! Your turn is over.')
                self.totalPoints += self.turnPoints
                break
            # select all remaining dice if fewer than 3 left
            elif len(self.dicePile) < 3:
                numDice = len(self.dicePile)
            # randomly select three dice
            else:
                numDice = 3
            for i in range(numDice):
                choice = random.choice(self.dicePile)
                self.dicePile.remove(choice)
                self.hand.append(choice)
            diceOutput = ''
            for dice in self.hand:
                dice.roll()
                diceOutput += '   ' + str(dice) + '\n'
                # dice with leaves on top put back into pile of unrolled dice
                if dice.get_top() == 'leaf':
                    self.dicePile.append(dice)
            # print dice rolled
            print(diceOutput[:-1])
            # add num dinos rolled to turn points and num feet rolled to num feet accumulated during turn
            dinos = [dice for dice in self.hand if dice.get_top() == 'dino']
            feet = [dice for dice in self.hand if dice.get_top() == 'foot']
            self.turnPoints += len(dinos)
            self.stomp += len(feet)
            self.hand = [] # empty hand for next roll
            # player stomped if more than 2 feet were rolled during turn
            if self.stomp > 2:
                print('Too bad -- you got stomped!')
                break
            else:
                # print player info
                print('This turn so far: ' + str(self.turnPoints) + ' dinos and ' + str(self.stomp) + ' feet.')
                print('You have ' + str(len(self.dicePile)) + ' dice remaining.')
                print(self.find_num_color())
                answer = ''
                # ask player if they want to roll again
                while answer not in ['y','n']:
                    answer = input('Do you want to roll again (y/n)? ')
                # end turn if not
                if answer == 'n':
                    self.totalPoints += self.turnPoints
                    break
   
def play_dino_hunt(numPlayers,numRounds):
    '''play_dino_hunt(numPlayer,numRounds)
    plays a game of Dino Hunt
      numPlayers is the number of players
      numRounds is the number of turns per player'''
    # set up players
    playerList = []
    for n in range(numPlayers):
        name = input('Player #' + str(n+1) + ', enter your name: ')
        playerList.append(DinoPlayer(name))
    currentPlayerNum = random.randrange(numPlayers) # randomly assign who goes first
    # play game
    for r in range(numRounds):
        print('\nROUND ' + str(r+1))
        for p in range(len(playerList)):
            print('')
            # print game status each turn
            for player in playerList:
                print(player)
            print('')
            playerList[currentPlayerNum].take_turn() # take a turn
            currentPlayerNum = (currentPlayerNum + 1) % numPlayers # go to next player
        # reset each player for next round
        for player in playerList:
            player.reset()
    # find winner
    mostPoints = -1
    for player in playerList:
        points = player.get_points()
        if points > mostPoints:
            mostPoints = points
            winner = player
    print('\nWe have a winner!')
    print(winner)

print(play_dino_hunt(2,2))
