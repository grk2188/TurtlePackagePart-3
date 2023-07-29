import random
from turtle import Turtle, Screen


t = Turtle()
screen = Screen()
#t.colormode(255)
colors = ["gold", "darkolivegreen", "red", "indigo", "coral", "yellow", "blue", "orange"]

t.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        t.color(random.choice(colors))
        t.circle(100)
        t.setheading(t.heading() + size_of_gap)

draw_spirograph(5)

screen.exitonclick()

