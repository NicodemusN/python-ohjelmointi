# Count Occurrences

# otetaan käyttäjän syöte
a = input("Anna sanoja muodossa sana1,sana2,sana3 ja niin edelleen: ")
lst = a.split(",")

# alustetaan dictionary
dct = {}

# loopataan jokainen listan jäsen
for i in lst:

    # setdefault() on toiminto, jolla voidaan lisätä
    # arvoja dictionaryyn riippuen siitä, onko "avain"
    # jo olemassa dictionaryssa

    dct.setdefault(i, 0) # listan ensimmäinen jäsen saa arvon 0
    dct[i] += 1 # arvoa lisätään yhdellä. jos jäsen tulee uudelleen
                # vastaan toisella loopin kierroksella, arvo kasvaa
                # jälleen yhdellä.
                # näin saadaan laskettua jokaisen syötetyn sanan määrä

print(dct)