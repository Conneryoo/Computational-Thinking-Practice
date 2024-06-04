import turtle
t=turtle.Turtle()
t.shape("turtle")

import random


for i in range(1, 31, 1):
    length=random.randint(1,100)
    angle=random.randint(-180,180)
    t.forward(length)
    t.left(angle)
