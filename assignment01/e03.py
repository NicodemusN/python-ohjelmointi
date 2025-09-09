# Ympyrä

import turtle

kilpikonna = turtle.Turtle()
kilpikonna.shape("turtle")

i = 0
# säteen muuttuja x
x = 10

while x < 100:
    kilpikonna.circle(x)
    x = x + 5