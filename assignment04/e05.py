# Toimii

def maximum (a, b, c):
    max = 0
    if a > 0:
        max = a
    if b > max:
        max = b
    if c > max:
        max = c
    print(max)

luku1 = int(input("Anna ensimmäinen luku: "))
luku2 = int(input("Anna toinen luku: "))
luku3 = int(input("Anna kolmas luku: "))

maximum(luku1, luku2, luku3)