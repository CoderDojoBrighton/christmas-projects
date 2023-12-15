import turtle

def draw(speed, x_offset_1, x_offset_2):
    light1 = turtle.Pen()
    light1.speed(speed)
    light1.shapesize(2,2,2)
    light2 = turtle.Pen()
    light2.speed(speed)
    light2.shapesize(2,2,2)
    light3 = turtle.Pen()
    light3.speed(speed)
    light3.shapesize(2,2,2)
    light4 = turtle.Pen()
    light4.speed(speed)
    light4.shapesize(2,2,2)
    light5 = turtle.Pen()
    light5.speed(speed)
    light5.shapesize(2,2,2)
    light6 = turtle.Pen()
    light6.speed(speed)
    light6.shapesize(2,2,2)

    light1.up()
    light1.setposition(x_offset_1,-20)
    light1.down()
    light1.hideturtle()

    light2.up()
    light2.setposition(x_offset_1,60)
    light2.down()
    light2.hideturtle()

    light3.up()
    light3.setposition(x_offset_1,130)
    light3.down()
    light3.hideturtle()

    light4.up()
    light4.setposition(x_offset_2,-20)
    light4.down()
    light4.hideturtle()

    light5.up()
    light5.setposition(x_offset_2,60)
    light5.down()
    light5.hideturtle()

    light6.up()
    light6.setposition(x_offset_2,130)
    light6.down()
    light6.hideturtle()

    # Flashing light
    colors = ['red','yellow','blue']
    counter = 0
    while counter < 50:
        light1.dot(20, colors[counter % 3])
        light4.dot(20, colors[counter % 3])
        light2.dot(20, colors[(counter + 1) % 3])
        light5.dot(20, colors[(counter + 1) % 3])
        light3.dot(20, colors[(counter + 2) % 3])
        light6.dot(20, colors[(counter + 2) % 3])
        counter = counter + 1
