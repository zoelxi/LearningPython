import random

def backgammon_roll():
    x=random.randrange(1,7)
    y=random.randrange(1,7)
    if x==y:
        return 4*x
    else:
        return x+y
    
def backgammon_roll_game():
    player1=0
    player2=0
    while True:
        store1=backgammon_roll()
        player1+=store1
        print('Player 1 rolled '+str(store1)+'\nThe score is: Player 1 has '+str(player1)+' , Player 2 has '+str(player2))
        if player1>=100:
            return 'Player 1 wins!'
        store2=backgammon_roll()
        player2+=store2
        print('Player 2 rolled '+str(store2)+'\nThe score is: Player 1 has '+str(player1)+' , Player 2 has '+str(player2))
        if player2>=100:
            return 'Player 2 wins!'

print(backgammon_roll_game())

        
