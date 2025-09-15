# Dictionary Lookup

ages = {"John": 25, "Mary": 30, "Alex": 22}

name = input("Anna nimi ")

if ages.get(name) != None:
    print(ages.get(name))
else:
    print("Nimeä ei löytynyt.")