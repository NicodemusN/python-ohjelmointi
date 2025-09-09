import random

salainen_luku = random.randint(1, 10)
kayttajan_syote = -1
yritys = 0

while kayttajan_syote != salainen_luku:
    print("Arvaa salainen luku (1 - 10)")
    kayttajan_syote = int( input() )
    yritys = yritys + 1

print("oikein!")
print("Arvasit " + str(yritys) + " kertaa.")