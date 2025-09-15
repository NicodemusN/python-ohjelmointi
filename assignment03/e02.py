# Shopping List

# luodaan lista aluksi tyhjänä
list = []

# pyydetään for-loopilla jokainen tuote erikseen
for _ in range(5):
    print("Anna tuote:")
    item = input()
    list.append(item)

print()
print("Ostoslista on: ")

# printataan nätisti iteroiden ostoslista
for x in list:
    print(x)