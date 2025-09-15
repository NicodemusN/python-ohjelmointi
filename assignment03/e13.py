# Set Operations

# pyydetään luvut käyttäjältä
print("Anna lukuja muodossa x,y,z,...")
pre1 = input()

print("Anna lukuja muodossa x,y,z,...")
pre2 = input()

# muutetaan käyttäjän antamat merkkijonot (string) listoiksi (list)
lst1 = pre1.split(",")
# print(lst1)
lst2 = pre2.split(",")
# print(lst2)

# muutetaan listat seteiksi (set)
set1 = set(lst1)
set2 = set(lst2)

print("Union: ", end="")
print(set1.union(set2))
print("Intersection: ", end="")
print(set1.intersection(set2))