# Tuodaan ulkoiset kirjastot
import tkinter
import turtle

# Luodaan kilpikonna
kilpikonna = turtle.Turtle()
kilpikonna.shape("turtle")

print("Anna suunta kilpikonnalle")
kysymys = input()
# Käytetään casefold, jolloin ei väliä onko isoja vai pieniä kirjaimia.
suunta = kysymys.casefold()

# Karmea boilerplate if-else hirviö
if suunta == "oikea":
    kilpikonna.forward(50)

elif suunta == "vasen":
    kilpikonna.left(180)
    kilpikonna.forward(50)

elif suunta == "alas":
    kilpikonna.right(90)
    kilpikonna.forward(50)

elif suunta == "ylös":
    kilpikonna.left(90)
    kilpikonna.forward(50)

tkinter.mainloop()