# Toimii

def filter_even(numbers):
    odds = list()               # tehdään parittomille luvuille oma lista
    for i in numbers:           # jokaista käyttäjän syöttämän listan lukua kohden
        if (i % 2 != 0):        # jos luku ei ole jaollinen kahdella (eli parillinen)
            odds.append(i)      # lisätään luku parittomien listaan
    return odds                 # funktio palauttaa parittomien listan


lst = list()                    # alustetaan lista käyttäjän syötteille
y = 1                           # alustetaan y positiiviseksi
while y > 0:                    # niin kauan kuin y on yli 0
    y = int(input("Anna positiivinen kokokonaisluku, lopetus negatiivisella: "))

    if y > 0:                   # jos käyttäjän antama luku on posiitivinen
        lst.append(y)           # lisätään luku listaan

print(filter_even(lst))         # kutsutaan funktio filter_even print-funktion sisällä
                                # jolloin funktion palautearvo odds tulee tulostetuksi