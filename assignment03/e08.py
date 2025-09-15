# Tuple with Mixed Data Types

myTuple = ("Alice", 30, [10, 20 ,30], True)

# tulostetaan tuple
print("Tuple: ", end="")
print(myTuple)

# erotetaan lista tuplen sisältä
list1 = myTuple[2]
print("Lista: ", end="")
print(list1)

# lisätään luku 40 listaan ja tulostetaan tuple
list1.append(40)
print("Päivitetty tuple: ", end="")
print(myTuple)