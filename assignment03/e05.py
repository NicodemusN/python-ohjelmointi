# Check Palindrome with List

print("Anna sana")
word = input()
letters = list(word)
letters2 = []

# otetaan sanan pituusta listasta for-loopille käyvässä muodossa
i = len(letters) -1

# iteroidaan annetun sana pituus lopusta alkuun
for x in range(len(letters), 0, -1):
    # lisätään uuteen "sanalistaan" kirjaimet annetusta sanasta
    letters2.append(letters[i])
    i -= 1
    
    # debug
    # print(letters2)

if letters2 == letters:
    print("Kyseessä on palindromi.")
else:
    print("Kyseessä ei ole palindromi.")