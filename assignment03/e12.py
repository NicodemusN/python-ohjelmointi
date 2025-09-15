# Set Membership Test

# luodaan set
name_list = {"Alice", "Bob", "Charlie"}

# kysytään nimi
print("Anna nimi")
name = input()

# tarkistetaan, onko nimi listassa
if name in name_list:
    print("Nimi sallittu.")
else:
    print("Nimi ei sallittu.")