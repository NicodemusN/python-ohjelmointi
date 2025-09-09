print("luku1")
luku1 = int(input())
print("luku2")
luku2 = int(input())

summa = sum([luku1, luku2])

if summa > 10:
    print("Yli 10")
elif summa == 10:
    print(10)
elif summa < 10:
    print("Alle 10")