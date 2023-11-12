import random
from character_classes import player, goblin
from game_fuctions import is_dead, ai_combat_choices, player_lose_hp, monster_lose_hp


def tutorial_combat():
    print(f"\t\nSystem: You have encounter a goblin!")
    print(f"\tName: {player.name}  \n\tHP: {player.health}")
    print(f"\n\tName: {goblin.name}  \n\tHP: {goblin.health}")

    while True:
        user_choice = input(f"\nPick your actions: \n[A]tk \n[G]uard \n")

        if user_choice == "A" or user_choice == "a":
            g_hp = goblin.health - player.atk
            monster_lose_hp(g_hp)

            print(f"{player.name}: deals {player.atk} to the {goblin.name}!")
            print(f"It lost {goblin.health} HP!")
        elif user_choice == "G" or user_choice == "g":
            print(f"{player.name} has decided to guard!")
        else:
            print("Invalid input. Try again.")
            continue

        if ai_combat_choices() == "atk":
            p_hp = player.health - goblin.atk
            player_lose_hp(p_hp)

            print(f"{goblin.name}: deals {goblin.atk} to you!")
            print(f"You lost {player.health} HP!")
        else:
            print(f"{goblin.name} has decided to guard!")

        print(f"\tName: {player.name}  \n\tHP: {player.health}")
        print(f"\n\tName: {goblin.name}  \n\tHP: {goblin.health}")

        if is_dead(player.health, goblin.health):
            return False

