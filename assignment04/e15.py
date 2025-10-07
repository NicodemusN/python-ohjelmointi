# Toimii

def tulosta(merkki, maara):
    for _ in range(maara):
        print(merkki, end="")

korkeus = int(input("Anna korkeus: "))

for rivi in range(korkeus):
    tulosta("X", korkeus)
    print()