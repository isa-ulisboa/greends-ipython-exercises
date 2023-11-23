# https://plainenglish.io/blog/learn-classes-by-making-a-game-in-python-5aedee38fc18

import random
import collections # to count frequencies


FIGHTER = {"health": 4, "attack": 2, "dodge": 1, "speed":4}
THIEF = {"health": 2, "attack": 3, "dodge": 4, "speed":4}
MAGE = {"health": 2, "attack": 5, "dodge": 4, "speed":3}

TYPES = {"fighter": FIGHTER, "thief": THIEF, "mage": MAGE}


class Character:
    """ _health = 0 # arbitrary value
    _attack = 0
    _dodge = 0 """

    def __init__(self, char_type):
        self._char_type = char_type
        #self._assign_attributes()
        type_dict = TYPES[self._char_type]
        self._health = type_dict["health"]
        self._attack = type_dict["attack"]
        self._dodge = type_dict["dodge"]
        self._speed = type_dict["speed"]

    def __str__(self):
        return self._char_type
    """ 
        def _assign_attributes(self):
            type_dict = TYPES[self._char_type]
            self._health = type_dict["health"]
            self._attack = type_dict["attack"]
            self._dodge = type_dict["dodge"]
    """
    def attack(self):
        return 0.2*self._speed*self._attack
    
    def sword_attack(self):
        return self._attack

    def take_damage(self, damage):
        if self._dodge_success():
            self._speed -= 2
            return "Missed!"
        self._health -= damage
        return f"{self._char_type} took {damage} damage."

    def _dodge_success(self):
        # Every point in dodge is 5% chance to dodge
        dodge_chance = self._dodge * 5
        dodge_roll = random.randint(1, 100)
        if dodge_roll <= dodge_chance:
            return True
        return False

    def is_dead(self):
        return self._health <= 0
    
    def update(self):
        type_dict = TYPES[self._char_type]
        self._speed=type_dict["speed"]


def character_fight(type_1, type_2):
    character_1 = Character(type_1)
    character_2 = Character(type_2)
    # choose who attacks first
    first, second = character_1, character_2
    if random.choice([0,1]):
        first, second = character_2, character_1
    """ 
        coin_toss = random.randint(0, 1)
        if coin_toss == 0:
            #first, second = [character_1, character_2]
            first, second = character_1, character_2
        else:
            first, second = character_2, character_1
    """    
    # battle until one of the characters die; the winner exits the fight
    while True:
        if attack_character(first, second):
            return str(first)
        if attack_character(second, first):
            return str(second)
        first.update()
        second.update()


def attack_character(first, second):
    damage = first.attack()
    second.take_damage(damage)
    if second.is_dead():
        return True
    return False


def main():
    char_1 = "fighter"
    char_2 = "mage"
    char_3 = "thief"
    winners=[]
    # go for N battles for each pair of characters
    N=1000
    for _ in range(N):
        winners.append(character_fight(char_1, char_2))
        winners.append(character_fight(char_1, char_3))
        winners.append(character_fight(char_2, char_3))
    # Frequency of wins
    print("Results:",dict(collections.Counter(winners)))

if __name__ == "__main__":
    main()
