# Remove Item from List
# Jatketaan aiemmasta koodista riviltä 20

# luodaan lista aluksi tyhjänä
list = []

# pyydetään for-loopilla jokainen tuote erikseen
for _ in range(5):
    print("Anna tuote:")
    item = input()
    list.append(item)

print()
print("Ostoslista on:")

# printataan nätisti iteroiden ostoslista
for x in list:
    print(x)

# pyydetään tuote poistettavaksi listalta
print("Anna tuote, jonka haluat poistaa listalta:")
removed_item = input()

# jos tuote on listalla --> tuote poisteen listalta, muuten annetaan virheviesti
if removed_item in list:
    list.remove(removed_item)
    print("Uusi ostoslista on:")
    for x in list:
        print(x)
else:
    print("Tuote ei ollut listalla.")