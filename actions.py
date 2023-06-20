
import random as r

def heal(Warrior):
    Warrior.health = Warrior.health + r.randint(1, 100)

def print_message(*args):
    print(*args, sep='\n')
    print()

