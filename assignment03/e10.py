# Nested Tuples

# luodaan tuple
students = (("Anna", 25, "Kone"), ("Pekka", 30, "Sähkö"))

# tulostetaan jokainen tuplen sisäisen tuplen jäsen oikealla syntaksilla
i = 0
for _ in range(len(students)):
    print("Nimi: ", end=" ")
    print(students[i][0], end=", ")
    print("Ikä: ", end=" ")
    print(students[i][1], end=", ")
    print("Ala: ", end=" ")
    print(students[i][2], end="")
    print()
    i += 1