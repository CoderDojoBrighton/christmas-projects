import turtle

# Set up screen
def draw(speed, x_offset):
    # Create turtle
    t = turtle.Pen()
    t.shapesize(2,2,2)
    t.speed(speed)

    # Top tree section
    t.up()
    t.setposition(x_offset + -60, 100)
    t.down()
    t.fillcolor('green')
    t.begin_fill()
    t.forward(120)
    t.left(130)
    t.forward(95)
    t.left(100)
    t.forward(95)
    t.end_fill()

    # Middle tree section
    t.up()
    t.setx(x_offset + -35)
    t.down()
    t.begin_fill()
    t.fd(100)
    t.lt(130)
    t.fd(200)
    t.lt(130)
    t.fd(100)
    t.end_fill()

    ## Bottom section
    t.up()
    t.setposition(x_offset + -45,24)
    t.down()
    t.begin_fill()
    t.lt(100)
    t.fd(130)
    t.lt(130)
    t.fd(260)
    t.lt(130)
    t.fd(130)
    t.end_fill()

    # Trunk
    t.up()
    t.setposition(x_offset + -30,-75)
    t.down()
    t.fillcolor('brown')
    t.begin_fill()
    t.lt(140)
    t.fd(50)
    t.lt(90)
    t.fd(60)
    t.lt(90)
    t.fd(50)
    t.end_fill()

    # Star on the top
    t.up()
    t.setposition(x_offset + -30,190)
    t.fillcolor('yellow')
    t.begin_fill()
    t.rt(90)
    t.down()
    for i in range(5):
        t.fd(60)
        t.rt(144)
    t.end_fill()

    # Baubles
    t.up()
    t.setposition(x_offset + -55, 100)
    t.down()
    t.dot(20, 'blue')

    t.up()
    t.setposition(x_offset + 55, 100)
    t.down()
    t.dot(20, 'purple')

    t.up()
    t.setposition(x_offset + -90, 20)
    t.down()
    t.dot(20, 'red')

    t.up()
    t.setposition(x_offset + 90, 20)
    t.down()
    t.dot(20, 'yellow')

    t.up()
    t.setposition(x_offset + 125, -80)
    t.down()
    t.dot(20, 'pink')

    t.up()
    t.setposition(x_offset + -125, -80)
    t.down()
    t.dot(20, 'orange')

    t.hideturtle()
