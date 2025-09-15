# List Average

sum = 0
list1 = []

# pyydetään käyttäjältä luvut
for _ in range(5):
    print("Anna luku")
    num = int(input())
    list1.append(num)

# summataan käyttäjän antamat luvut listasta
i = 0
for x in range(len(list1)):
    sum = sum + list1[i]
    i += 1

# tehdään laskutoimitus ja tulostetaan keskiarvo
average = sum / len(list1)
print("Lukujen keskiarvo on ", end="")
print(average)