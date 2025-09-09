print("Anna kuukausi:")
month = int(input())
print("Anna päivä:")
day = int(input())

if (month == 12 and day == 6) or (month == 5 and day == 1):
    print("Nyt on vappu tai itsenäisyyspäivä.")
else:
    print("Nyt ei ole vappu tai itsenäisyyspäivä.")