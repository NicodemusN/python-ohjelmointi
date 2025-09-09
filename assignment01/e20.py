# alustetaan muuttujat
pienin = 0
luku = 0

# ohjelma halutaan lopettaa negatiivisella luvulla,
# joten loop pidetään aktiivisena niin kauan kuin
# annettavat luvut ovat positiivisia tai 0
while luku >= 0:
    print("Anna positiivinen numero (lopetus negatiivisella luvulla)")
    luku = int( input() )
    # muuttuja "pienin" saa uuden arvon, jos annettu
    # luku on 0 tai pienempi kuin viimeksi annettu
    # luku. Luvun pitää silti olla vähintään 0,
    # jotta se voidaan antaa muuttujalle "pienin"
    if pienin == 0 or (luku < pienin and luku >= 0):
        pienin = luku

# varmistetaan, että "pienin" ei ole negatiivinen luku
if pienin >= 0:
    print("Pienin antamasi luku oli ")
    print(pienin)

# jos sopivia lukuja ei annettu, ohjelma antaa virheviestin
else:
    print("Et antanut lukuja.")