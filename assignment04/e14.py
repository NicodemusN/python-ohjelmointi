# Toimii

def merkit(c, n):
    for i in range(n):
        print(c, end="")
    print()

a1 = input("Anna merkki: ")
a2 = int(input("Anna lukumäärä: "))

merkit(a1, a2)