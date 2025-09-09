print("Anna arvosanasi")
arvosana = int(input())
if arvosana == 0:
    print("Tavoitteet ovat saavuttamatta.")
elif arvosana == 1:
    print("Olet saavuttanut tavoitteet osittain.")
elif arvosana == 2:
    print("Olet saavuttanut tavoitteet hyvin.")
elif arvosana == 3:
    print("Olet saavuttanut tavoitteet kiitettävästi.")
else:
    print("Annoit väärän arvosanan.")
