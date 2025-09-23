# Nested Dictionary

# alustetaan dictionary

students = {
    "Alice": {"age": 21, "major": "CS"},
    "Bob": {"age": 22, "major": "Math"}
}

dct = dict()
dct2 = dict()

# "main loop"
run = 0
while run < 2:
    print("[1] Lisää uusi opiskelija")
    print("[2] Exit")
    run = int(input())
    
    if run == 1:
        name = input("Anna nimi: ")
        age = int(input("Anna ikä: "))
        major = input("Anna ala: ")

        dct["age"] = age
        dct["major"] = major

    students[name] = dct

print(dct)
print(students)