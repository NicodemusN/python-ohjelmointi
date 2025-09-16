# Convert List to Dict

# alustetaan list ja dictionary
lst = []
dct = {}

# luodaan lista
for _ in range(3):
    a = input("Anna avain-arvo pari (muodossa x:y): ")
    # seuraava erottelee annetut avain-arvoparit omiksi listoikseen luodun listan sisälle
    lst.append(a.split(":"))

# debug
# print(lst)

# loopataan listan pituuden verran ja luodaan uusia
# dictionaryn jäseniä listan sisäisten listojen jäsenistä
for i in range(len(lst)):
    x = lst[i][0]
    dct[x] = lst[i][1]

# tulostetaan dictionary
print(dct)