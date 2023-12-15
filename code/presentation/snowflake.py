# https://projects.raspberrypi.org/en/projects/turtle-snowflakes/7
import random
import turtle

def draw(distance, start_angle, speed=0):
    t = turtle.Pen()
    t.speed(speed)
    t.shapesize(2,2,2)

    t.up()
    t.left(start_angle)
    t.forward(distance)
    t.setheading(90)

    t.forward(90)
    t.left(45)
    t.down()

    for _ in range(8):
        branch(t)
        t.left(45)

    t.hideturtle()

    

def branch(t):
    for _ in range(3):
        for _ in range(3):
            t.forward(30)
            t.backward(30)
            t.right(45)
        t.left(90)
        t.backward(30)
        t.left(45)
    t.right(90)
    t.forward(90)