import turtle

# Create the screen
window = turtle.Screen()

# Create the pen (turtle) and set speed
pen = turtle.Turtle()
pen.speed(0)

# Set the background to blue
window.bgcolor("skyblue")


# Draw a circle with a center (x, y), radius and colour
def draw_circle(x, y, radius, pen_color, fill_color):
    # Set the pen to a colour
    pen.color(pen_color)
    # Fill in what we draw
    pen.fillcolor(fill_color)
    pen.begin_fill()

    # Move without drawing
    pen.penup()

    # Move and start drawing
    pen.setposition(x, y)
    pen.pendown()

    # Draw a circle with radius 150 and fill it
    pen.circle(radius)

    pen.end_fill()


# Lower body
draw_circle(0, -395, 150, "white", "white")
# Middle body
draw_circle(0, -140, 100, "white", "white")
# Head
draw_circle(0, 30, 70, "white", "white")

# Left eye
draw_circle(-30, 110, 8, "black", "black")
# Right eye
draw_circle(30, 110, 8, "black", "black")

# Mouth
draw_circle(-25, 75, 2, "black", "black")
draw_circle(-15, 70, 2, "black", "black")
draw_circle(-5, 68, 2, "black", "black")
draw_circle(5, 68, 2, "black", "black")
draw_circle(15, 70, 2, "black", "black")
draw_circle(25, 75, 2, "black", "black")

# Buttons
draw_circle(0, -20, 8, "black", "black")
draw_circle(0, -50, 8, "black", "black")
draw_circle(0, -80, 8, "black", "black")

# Nose
pen.color("orange")
pen.fillcolor("orange")
pen.penup()
pen.setposition(0, 105)
pen.begin_fill()
pen.pendown()
pen.right(150)
pen.forward(30)
pen.left(150)
pen.forward(30)
pen.goto(0, 105)
pen.end_fill()

# Hat
pen.color("black")
pen.fillcolor("black")
pen.begin_fill()
pen.penup()
pen.pensize(5)
pen.setposition(0, 150)
pen.pendown()
pen.forward(75)
pen.left(90)
pen.forward(10)
pen.left(90)
pen.forward(40)
pen.right(90)
pen.forward(60)
pen.left(90)
pen.forward(70)
pen.left(90)
pen.forward(60)
pen.right(90)
pen.forward(40)
pen.left(90)
pen.forward(10)
pen.left(90)
pen.goto(0, 150)
pen.end_fill()
# Ribbon
pen.color("red")
pen.fillcolor("red")
pen.begin_fill()
pen.penup()
pen.setposition(1, 165)
pen.pendown()
pen.forward(34)
pen.left(90)
pen.forward(10)
pen.left(90)
pen.forward(70)
pen.left(90)
pen.forward(10)
pen.setposition(1, 165)
pen.end_fill()

# Arms
def draw_arm(x, y, pen_color):
    pen.color(pen_color)
    pen.pensize(7)
    pen.penup()
    pen.setposition(x, y)
    pen.pendown()
    pen.left(115)
    pen.forward(100)
    pen.left(45)
    pen.forward(30)
    pen.right(180)
    pen.forward(30)
    pen.left(90)
    pen.forward(30)
    pen.left(180)
    pen.forward(30)
    pen.right(130)
    pen.forward(30)

# Right arm
draw_arm(70, -40, "chocolate")
# Left arm
draw_arm(-70, -40, "chocolate")

# Keep the window open when done drawing
turtle.done()
