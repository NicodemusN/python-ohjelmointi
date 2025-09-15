# Set Creation

# alustetaan set "constructor" tavalla (jos käyttäisi {}-sulkeita, niin datatyyppi olisi alustettaessa dictionary)
mySet = set()

# kysytään jokainen sana settiin erikseen
for _ in range(5):
    print("Anna sana")
    word = input()
    mySet.add(word)

# tulostetaan set
print(mySet)

# lopuksi huomataan, että duplikaatit poistuvat automaattisesti