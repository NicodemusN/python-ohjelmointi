# List of Dictionaries

# luodaan lista

products = [
    {"name": "milk", "price": 1.5},
    {"name": "bread", "price": 2.0}
]

i = 0
#for i in products[i]:
#    print(products[i][0], end=" ")
#    print("costs", end="")
#    print(products[i][1])

j = 0
for y in range(len(products)):
    for x in products[i]:
        print(products[i][x], end=" ")
        if j == 0:
            print("costs", end=" ")
        j += 1