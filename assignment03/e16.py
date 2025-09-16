# Dictionary from Input

ages = {}

for _ in range(3):
    a = input("Anna nimi: ")
    b = input("Anna pisteet: ")

    ages.update({a: b})

print(ages)