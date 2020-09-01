import random

class Pokemon:

    def __init__(self,name,startHealth,att,defense):
        self.name = name
        self.health = startHealth
        self.att = att
        self.defense = defense

    def __str__(self):
        return str(self.name) + ' has ' + str(self.health) + ' health, ' + str(self.att) + ' attack, and ' + str(self.defense) + ' defense.'

    def calculate_damage(self,other):
        r = random.uniform(0.85,1)
        return ((12/5)*(self.att/other.defense)+2)*r

    def attack(self,other):
        damage = int(self.calculate_damage(other))
        other.health -= damage
        print(str(self.name) + ' does ' + str(damage) + ' damage!')
        if other.health <= 0:
            print(str(other.name) + ' has fainted!')




