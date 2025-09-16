# Check Palindrome with List

print("Anna sana")
word = input()
letters = list(word)
letters2 = []

# otetaan sanan pituusta listasta for-loopille käyvässä muodossa
i = len(letters) -1
# pitää vähentää yksi, koska for loop laske 0, 1, 2...n
# eli jos sanassa on 3 kirjainta, niin for loop luulee
# on 4, koska 0, 1, 2, 3

# iteroidaan annetun sana pituus lopusta alkuun
for x in range(len(letters), 0, -1):
    # lisätään uuteen "sanalistaan" kirjaimet annetusta sanasta
    # väärässä järjestyksessä
    letters2.append(letters[i])
    i -= 1
    
    #debug
    #print(letters2)

if letters2 == letters:
    print("Kyseessä on palindromi.")
else:
    print("Kyseessä ei ole palindromi.")