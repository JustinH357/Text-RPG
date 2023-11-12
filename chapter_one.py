import random
from character_classes import player, goblin, display_stats
from tutorial_battle import tutorial_combat


def ChapterOne():
    print("\t Text RPG Test \t")
    print("Where.... am I?")
    print("System: Welcome to TowerG, you are one of the chosen players to complete the tutorial to receive skills to "
          "complete the towers on Earth.")

    player.name = input("System: What is your name? ")

    print(f"Player name \"{player.name}\" successfully added.")
    print("\t\n** The tutorial will now start **")
    print(f"{player.name}: Looks like I am on the first floor of the tutorial. Let's see if I can see "
          f"my stats.")
    print(f"{player.name}: Okay I think all I need to do is say \"display status\"")

    display_stats(player.name, player.health, player.atk)

    print(f"{player.name}: Time to start the tutorial")

    tutorial_combat()
