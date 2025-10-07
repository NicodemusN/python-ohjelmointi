# Print Function

def merkit(c, n):
    for i in range(len(n)):
        print(c, end="")

a1 = input("Anna merkki: ")
a2 = input("Anna lukumäärä: ")

merkit(a1, a2)