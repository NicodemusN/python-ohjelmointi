# Add Item to List
# Ask the user to input a fruit to add, and add it to the list. Print the updated list.
#Enter a fruit to add: mango

# luodaan lista
fruits = ["apple", "banana", "orange", "mango"]
print("Hedelmälistä on: ")

# printataan jokainen listan jäsen nätisti
for x in fruits:
    print(x, end=" ")
print()

# pyydetään syöttämään uusi jäsen listalle
print("Syötä uusi hedelmä listalle: ")
new_fruit = input()
fruits.append(new_fruit)

# printataan lista uudella jäsenellä lisättynä
print("Uusi hedelmä lista on:")
for x in fruits:
    print(x, end=" ")
print()