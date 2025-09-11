print("Anna pistemäärä väliltä 0 - 60")
score = 0

while score <= 60 and score >= 0:
    score = int(input())
    if score <= 8:
        print("improbatur")
    elif score <= 16:
        print("approbatur")
    elif score <= 24:
        print("lubenter")
    elif score <= 35:
        print("cum laude")
    elif score <= 44:
        print("magna")
    elif score <= 52:
        print("eximia")
    elif score <= 60:
        print("laudatur")
    print("Anna uusi pistemäärä")
    