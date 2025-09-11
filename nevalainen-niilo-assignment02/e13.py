import random

a = None
games = 0
computer_wins = 0
player_wins = 0

while games < 3 and (player_wins < 2 or computer_wins < 2):
    choice = random.choice(["kivi", "paperi", "sakset"])
    print("Arvaa kivi, paperi tai sakset.")
    a = input()
    print("Tietokone vastasi: " + choice)
    if a == "kivi" and choice == "paperi":
        computer_wins += 1
    elif a == "kivi" and choice == "sakset":
        player_wins += 1
    elif a == "paperi" and choice == "sakset":
        computer_wins += 1
    elif a == "paperi" and choice == "kivi":
        player_wins += 1
    elif a == "sakset" and choice == "kivi":
        computer_wins += 1
    elif a == "sakset" and choice == "paperi":
        player_wins += 1
    games += 1

if player_wins > computer_wins:
    print("Voitit!")
elif computer_wins > player_wins:
    print("Tietokone voitti.")
else:
    print("Tasapeli.")