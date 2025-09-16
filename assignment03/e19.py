# Count Occurrences

a = input("Anna sanoja muodossa sana1,sana2,sana3 ja niin edelleen: ")
lst = a.split(",")

dct = {}

for i in range(len(lst)):
    x = lst[i]
    dct[x] = 0


print(dct)