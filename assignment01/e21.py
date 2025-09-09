#!/bin/python3

print("Anna suorakaiteen korkeus")
korkeus = int( input() )
print("Anna suorakaiteen leveys")
leveys = int( input() )

rivi = 0

while rivi < korkeus:
    sarake = 0
    while sarake < leveys:
        print("X", end='')
        sarake = sarake + 1
    
    print()
    rivi = rivi + 1