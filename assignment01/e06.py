# Pyydetään käyttäjän syöte
print("Anna luku 1")
luku1 = int(input())
print("Anna luku 2")
luku2 = int(input())
print("Anna luku 3")
luku3 = int(input())

# Lasketaan keskiarvo
average = sum([luku1, luku2, luku3]) / 3

# Tulostetaan keskiarvo
print("Lukujen keskiarvo on " + str(average))