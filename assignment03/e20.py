# Nested Dictionary

# alustetaan dictionary

students = {
    "Alice": {"age": 21, "major": "CS"},
    "Bob": {"age": 22, "major": "Math"}
}

# "main loop"
run = 0
while run < 2:
    print("[1] Lisää uusi opiskelija")
    print("[2] Exit")
    run = int(input())
    
    if run == 1:
        dct = dict()                        # tehdään uusi dictionary

        name = input("Anna nimi: ")         # tallennetaan käyttäjän syötteet muuttujiin
        age = int(input("Anna ikä: "))
        major = input("Anna ala: ")

        dct["age"] = age                    # tallennetaan muuttujat uuden dictionaryn jäseniksi
        dct["major"] = major
        students[name] = dct                # tallennetaan students dictionaryyn luotu uusi dictionary

#debug
#print(dct)
print(students)