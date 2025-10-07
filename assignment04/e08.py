# Toimii

# kaikki englanninkieliset vokaalit
vowels = ["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"]

a = input("Anna merkkijono: ")

def count_vowels(text):
    x = 0                   # x on vokaalien määrä, aluksi 0
    for i in text:          # jokaista merkkijonon merkkiä kohden, looppi
        if i in vowels:     # jos merkki on vowels-listassa (eli vokaali)
            x += 1          # lisätään vokaalien määrään yksi
    return x                # funktio palauttaa vokaalien määrän arvon

print("Vokaalien määrä: ", end="")
print(count_vowels(a))      # kutsutaan funktio printtaamalla sen palautearvo