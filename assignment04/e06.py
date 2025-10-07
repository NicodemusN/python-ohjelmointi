# Toimii

# määritellään funktio joka laskee keskiarvon
def average(numbers):
    sum = 0
    for i in range(len(numbers)):
        sum = sum + lst[i]
    avr = sum / len(numbers)
    return avr

# alustetaan lista
lst = list()

# kysytään käyttäjän syöte ja lisätään listaan
for i in range(5):
    a = int(input("Anna luku " + str(i+1) + ": "))
    lst.append(a)

# tulostetaan keskiarvo kutsumalla funktio
print("Antamiesi lukujen keskiarvo on ", end="")
print(average(lst))

#debug
#print(lst)