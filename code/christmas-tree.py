import turtle

# Set up screen
width = 500
height = 500
s = turtle.Screen()
s.setup(width, height)
s.title("Christmas Tree!")

# Create turtle
t = turtle.Pen()
t.speed(2)

# Top tree section
t.up()
t.setposition(-60, 100)
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
t.setx(-35)
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
t.setposition(-45,24)
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
t.setposition(-30,-75)
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
t.setposition(-30,190)
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
t.setposition(-55, 100)
t.down()
t.dot(20, 'blue')

t.up()
t.setposition(55, 100)
t.down()
t.dot(20, 'purple')

t.up()
t.setposition(-90, 20)
t.down()
t.dot(20, 'red')

t.up()
t.setposition(90, 20)
t.down()
t.dot(20, 'yellow')

t.up()
t.setposition(125, -80)
t.down()
t.dot(20, 'pink')

t.up()
t.setposition(-125, -80)
t.down()
t.dot(20, 'orange')

t.hideturtle()

# Flashing  Lights
light1 = turtle.Pen()
light2 = turtle.Pen()
light3 = turtle.Pen()

light1.up()
light1.setposition(0,-20)
light1.down()
light1.hideturtle()

light2.up()
light2.setposition(0,60)
light2.down()
light2.hideturtle()

light3.up()
light3.setposition(0,130)
light3.down()
light3.hideturtle()

# Flashing light
colors = ['red','yellow','blue']
counter = 0
while True:
    light1.dot(20, colors[counter % 3])
    light2.dot(20, colors[(counter + 1) % 3])
    light3.dot(20, colors[(counter + 2) % 3])
    counter = counter + 1

turtle.mainloop()
