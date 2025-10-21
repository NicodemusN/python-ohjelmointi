age = int(input("Anna ikäsi: "))
a = input("Onko sinulla opiskelijakortti, yes/no: ")
card = False

if a == "yes":
    card = True

if age < 18 and card == True:
    print("Saat alennuksen.")
else:
    print("Et saa alennusta.")