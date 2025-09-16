# List of Dictionaries

# luodaan ostoslista

products = [
    {"name": "milk", "price": 1.5},
    {"name": "bread", "price": 2.0}

    # debug
    # {"name": "eggs", "price": 3.0}
]

# alustetaan muuttujat iteroinnille
i = 0
j = 0

# ei mitää hajua miten sain tän toimimaan
for y in products:
    for x in products[i]:
        print(products[i][x], end=" ")
        if j == 0:
            print("costs", end=" ")
        j += 1
    i += 1
    j = 0
    print() # uus rivi seuraaville ostoslistan esineille