import random


class BaseCharactersStats:
    def __init__(self, health, atk, name):
        self.health = health
        self.atk = atk
        self.name = name

    # set new values and set negative hp to 0
    def set_heath(self, new_health):
        if new_health < 0:
            new_health = 0
        self.health = new_health

    def set_atk(self, new_atk):
        self.atk = new_atk

    def set_name(self, new_name):
        self.name = new_name


player = BaseCharactersStats(100, 35, "no name")
goblin = BaseCharactersStats(80, 20, "Goblin")


def display_stats(player_name, player_hp, player_atk):
    print(f"\nName: {player_name} \nHP: {player_hp}  \nAtk: {player_atk}")
