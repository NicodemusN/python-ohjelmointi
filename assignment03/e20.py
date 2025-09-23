# Nested Dictionary

# alustetaan dictionary

students = {
    "Alice": {"age": 21, "major": "CS"},
    "Bob": {"age": 22, "major": "Math"}
}

lst = list()

# "main loop"
run = 0
while run < 2:
    print("[1] Lisää uusi opiskelija")
    print("[2] Exit")
    run = int(input())
    
    if run == 1:
        name = input("Anna nimi: ")
        age = input("Anna ikä: ")
        major = input("Anna ala: ")

        lst.insert(0, name)
        lst.insert(1, age)
        lst.insert(2, major)

print(lst)