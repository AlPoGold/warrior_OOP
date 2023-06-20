
from functools import total_ordering
import random as r

@total_ordering
class Warrior:

    def __init__(self, name, power=1, health=100):
        self._name = name
        self._power = power
        self._health = health
        self._level = 1



    def __str__(self):
        return f'Warrior, which name is {self._name}, has {self._power} power and {self._health} health'

    def __repr__(self):
        return f'Warrior(power={self._power}, health={self._health})'

    def __eq__(self, other):
        if isinstance(other, Warrior):
            return self._power == other._power
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Warrior):
            return self._power < other._power
        return NotImplemented

    def attack(self, enemy_strike):
       self._health = self._health - enemy_strike*self._power


    def alive(self):
        if self._health > 0:
            return True
        else:
            return False




