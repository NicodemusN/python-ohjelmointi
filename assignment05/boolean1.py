vkp = input("Anna viikonpäivä (mon, tue, ..., sun): ")
a = input("Onko vapaapäivä yes/no: ")
vpp = False

if a == "yes":
    vpp = True

if vkp == "sat" or vkp == "sun" or vpp == True:
    print("Voit levätä.")
else:
    print("Täytyy tehä töitä.")