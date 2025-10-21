temp = int(input("Anna päivän lämpötila: "))

if temp < 20:
    if temp < 0:
        print("It is freezing!")
    else:
        print("It is cold.")
else:
    print("It is warm.")