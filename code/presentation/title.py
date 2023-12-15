import turtle

def draw(speed):
    t = turtle.Pen()
    t.color("red")
    t.shapesize(2,2,2)
    t.up()
    t.speed(speed)
    # t.sety(400)
    t.left(90)
    t.forward(400)
    t.write("CoderDojo Christmas", align="center", font=("Mountains of Christmas", 100, "normal"))
    t.hideturtle()
