print("Anna luku:")
luku = int(input())

print("Lukujono:")
if luku > 0:
    while luku >= 0:
        print(luku)
        luku = luku - 1
elif luku < 0:
    while luku <= 0:
        print(luku)
        luku = luku + 1
else:
    print("Väärä syöte.")