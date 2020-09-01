import random

class Domino:
    
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        self.domino = (num1,num2)

    def __str__(self):
        return str(self.num1) + '-' + str(self.num2)

    def is_double_6(self):
        self.domino = (6,6)

    def is_left_match(self,other):
        if self.num1 == other.num1:
            (self.num1,self.num2) = (self.num2,self.num1)
        return (self.num2 == other.num1)

    def is_right_match(self,other):
        if self.num2 == other.num2:
            (self.num2,self.num1) = (self.num1,self.num2)
        return (self.num1 == other.num2)
    
class DominoSet:

    def __init__(self):
        self.dSet = []
        lower = 0
        for num1 in range(7):
            for num2 in range(lower,7):
                self.dSet.append(Domino(num1,num2))
            lower += 1
        random.shuffle(self.dSet)

    def __str__(self):
        return 'The domino set has ' + str(len(self.dSet)) + ' dominoes remaining.'

    def deal_domino(self):
        return self.dSet.pop()

class DominoChain:

    def __init__(self):
        self.chain = []

    def __str__(self):
            output = ''
            for domino in self.chain:
                output += str(domino) + ','
            output = output[:-1]
            return output
                
    def left_end(self):
        if len(self.chain) > 0:
            return self.chain[0]

    def right_end(self):
        if len(self.chain) > 0:
            return self.chain[-1]

    def add_left_domino(self,domino):
        if len(self.chain) == 0:
            self.chain.append(domino)
        if domino.is_left_match(self.left_end()):
            self.chain.insert(0,domino)

    def add_right_domino(self,domino):
        if len(self.chain) == 0 or domino.is_right_match(self.right_end()):
            self.chain.append(domino)
        
class DominoPlayer:

    def __init__(self,name,comp,dSet):
        self.name = name
        self.hand = [dSet.deal_domino() for i in range(7)]
        self.comp = comp
        self.length = 0
        self.draw = 0

    def __str__(self):
        return str(self.name) + ' has ' + str(len(self.hand)) + ' dominoes.'

    def get_name(self):
        return self.name

    def get_hand(self):
        output = ''
        for domino in self.hand:
            output += str(domino) + '\n'
        return output

    def find_double_6(self):
        for domino in self.hand:
            if domino.domino == (6,6):
                return True

    def play_double_6(self,chain):
        for domino in self.hand:
            if domino.domino == (6,6):
                self.hand.remove(domino)
                chain.add_right_domino(domino)
            
    def play_left_domino(self,domino,chain):
        self.hand.remove(domino)
        chain.add_left_domino(domino)

    def play_right_domino(self,domino,chain):
        self.hand.remove(domino)
        chain.add_right_domino(domino)

    def has_won(self):
        return self.draw == 1 or len(self.hand) == 0

    def take_turn(self,dSet,chain):
        if self.comp:
            print("It's Computer " + self.name + "'s turn.")
            print(chain)
            left = chain.left_end()
            right = chain.right_end()
            leftMatches = [domino for domino in self.hand if domino.is_left_match(left)]
            rightMatches = [domino for domino in self.hand if domino.is_right_match(right)]
            if len(leftMatches) + len(rightMatches) > 0:
                if len(leftMatches) > len(rightMatches):
                    self.play_left_domino(leftMatches[0],chain)
                    print('Computer ' + self.name + ' played the ' + str(leftMatches[0]) + ' domino.')
                else:
                    self.play_right_domino(rightMatches[0],chain)
                    print('Computer ' + self.name + ' played the ' + str(rightMatches[0]) + ' domino.')
            else:
                print('Computer ' + self.name + " can't play!")
                if self.length == len(chain.chain):
                    self.draw += 1
            self.length = len(chain.chain)
        else:
            print(self.name + ", it's your turn.")
            print(chain)
            print('Your hand: ')
            print(self.get_hand())
            left = chain.left_end()
            right = chain.right_end()
            leftMatches = [domino for domino in self.hand if domino.is_left_match(left)]
            rightMatches = [domino for domino in self.hand if domino.is_right_match(right)]
            if len(leftMatches) + len(rightMatches) > 0:
                lOrR = ''
                while lOrR not in ['l','r']:
                    lOrR = input('Do you want to attach a domino to the left or right end of the chain (l/r)? ')
                if (lOrR == 'l' and len(leftMatches) > 0) or len(rightMatches) == 0:
                    if lOrR == 'r':
                        print('Oh no! None of your dominoes can be attached to the right end of the chain. Try the left end instead.')
                    for index in range(len(leftMatches)):
                        print(str(index + 1) + ': ' + str(leftMatches[index]))
                    choice = 0
                    while choice < 1 or choice > len(leftMatches):
                        choiceStr = input('Which domino do you want to play? ')
                        if choiceStr.isdigit():
                            choice = int(choiceStr)
                    self.play_left_domino(leftMatches[choice-1],chain)
                elif (lOrR == 'r' and len(rightMatches) > 0) or len(leftMatches) == 0:
                    if lOrR == 'l':
                        print('Oh no! None of your dominoes can be attached to the left end of the chain. Try the right end instead.')
                    for index in range(len(rightMatches)):
                        print(str(index + 1) + ': ' + str(rightMatches[index]))
                    choice = 0
                    while choice < 1 or choice > len(rightMatches):
                        choiceStr = input('Which domino do you want to play? ')
                        if choiceStr.isdigit():
                            choice = int(choiceStr)
                    self.play_right_domino(rightMatches[choice-1],chain)
            else:
                if self.length == len(chain.chain):
                    self.draw += 1
                print("Oh no! You can't play, so you must pass.")
                input('Press enter to continue. ')
            self.length = len(chain.chain)

class Game:

    def __init__(self):
        self.players = 4

    def __str__(self):
        return 'Four players are playing dominoes.'

    def play_dominoes(self):
        dSet = DominoSet()
        chain = DominoChain()
        playerList = []
        for n in range(4):
            name = input('Player ' + str(n+1) + ', please enter your name: ')
            qComp = ''
            while qComp not in ['y','n']:
                qComp = input('Would you like ' + name + ' to be a computer-controlled player (y/n)? ')
            if qComp == 'y':
                comp = True
            else:
                comp = False
            playerList.append(DominoPlayer(name,comp,dSet))
        for player in playerList:
            if player.find_double_6():
                player.play_double_6(chain)
                print('\n' + player.get_name() + ' started the game with the 6-6 domino!\n')
                currentPlayerNum = (playerList.index(player) + 1) % 4      
        while True:
            print('----------')
            for player in playerList:
                print(player)
            print('----------')
            playerList[currentPlayerNum].take_turn(dSet,chain)
            if playerList[currentPlayerNum].has_won():
                print(chain)
                print(playerList[currentPlayerNum].get_name() + ' wins!')
                print('Thanks for playing! See you soon!')
                break
            else:
                currentPlayerNum = (currentPlayerNum + 1) % 4

g = Game()
g.play_dominoes()
        
