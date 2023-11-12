from character_classes import player, goblin
import random


def ai_combat_choices():
    goblin_options = ["atk", "guard"]
    goblin_choice = random.choice(goblin_options)
    return goblin_choice


def player_lose_hp(player_hp_lost):
    if player_hp_lost < player.health:
        player.set_heath(player_hp_lost)
    return player_hp_lost


def monster_lose_hp(monster_hp_lost):
    if monster_hp_lost < goblin.health:
        goblin.set_heath(monster_hp_lost)
    return monster_hp_lost


# true if death is detected
def is_dead(player_hp, monster_hp):
    if player_hp == 0:
        print("You lost the match. You died!")
        return True
    elif monster_hp == 0:
        print("You won the fight!")
        return True
    else:
        return False



