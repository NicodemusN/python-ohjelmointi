def tulosta(merkki, maara):
    for _ in range(maara):
        print(merkki, end="")

korkeus = int(input("anna korkeus"))

for rivi in range(korkeus):
    if rivi == 0 or rivi == korkeus -1:
        tulosta("X", korkeus)
    else:
        print("X", end="")
        tulosta(" ", korkeus - 2)
        print("X", end="")
    print()