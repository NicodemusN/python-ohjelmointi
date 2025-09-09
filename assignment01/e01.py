# Luodaan kilpikonna
import tkinter
import turtle
kilpikonna = turtle.Turtle()

kilpikonna.shape("turtle")

i = 0
while i < 4:
    # Mene eteenpäin 50 pikseliä
    kilpikonna.forward(50)

    # Käänny vasemmalle 90 astetta
    kilpikonna.left(90)
    i = i+1

tkinter.mainloop()