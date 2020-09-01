import random

def backgammon_roll():
    x=random.randrange(1,7)
    y=random.randrange(1,7)
    if x==y:
        return 4*x
    else:
        return x+y

print(backgammon_roll())
