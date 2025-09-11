print("Anna kellonajan tunnit")
hour = int(input())
print("Anna kellonajan minuutit")
min = int(input())
print("Anna rahamäärä euroissa")
money = int(input())

#isHourOk = False
#isTimeOk = True

if hour in range(12, 24) or hour in range(0, 3):
    isHourOk = True
elif hour == 3 and min <= 29:
    isTimeOk = True
else:
    isHourOk = False

if isHourOk == True and min in range (0, 60):
    isTimeOk = True
else:
    isTimeOk = False

if isTimeOk == True:
    if money >= 5:
        print("Pubi on auki klo 12 ja 03:29 välillä.", end="")
        print(" Kalja maksaa 5€. Mene pubiin.")
    elif money < 5:
        print("Sinulla on rahat loppu")
else:
    print("Nyt ei ole oikea kellonaika.")
