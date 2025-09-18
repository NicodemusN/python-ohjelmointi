
# Laskin kahden maapallon pisteen väliselle suorimmalle matkalle maan pintaa pitkin
# Ohjelmaan syötetään pisteiden koordinaatit asteiden tarkkuudella

import math

# Käyttöohje
print("Arvot x-akselilla ovat pituusasteita ja arvot y-akselilla ovat leveysasteita.")
print("Läntiset pituuspiirit ja eteläiset leveyspiirit on annettava negatiivisina ja desimaalimuodossa (esim. 75.23 ja 12.45).")

input1 = input("Anna ensimmäisen pisteen koordinaatit y,x: ")
input2 = input("Anna toisen pisteen koordinaatit y,x: ")

# input ja vakiomuuttujat
k1 = input1.split(",")
k2 = input2.split(",")

r_earth = 6371
theta = 0

# koordinaattien erottelu desimaaliluvuiksi
for i in range(len(k1)):
    k1[i] = float(k1[i])
    k1[i] = math.radians(k1[i])
i = 0
for i in range(len(k2)):
    k2[i] = float(k2[i])
    k2[i] = math.radians(k2[i])

# debug
print(k1)
print(k2)

# laskuosuus
# d = r cos-1[cos a cos b cos(x-y) + sin a sin b]

#dif_lat = k1[0] - k2[0]
dif_lon = k1[1] - k2[1]
#
#def haversine(val):
#    val = (1 - math.cos(val)) / 2
#    
#hav_dif_lat = haversine(dif_lat)
#hav_dif_lon = haversine(dif_lon)

d = r_earth * math.acos(math.acos(k1[0]) * math.acos(k2[0])* math.acos(dif_lon) + math.sin(k1[0]) * math.sin(k2[0]))
print(d)