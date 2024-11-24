import turtle

# Create the screen
s = turtle.Screen()
width = 500
height = 500
s.setup(width, height)
s.title("Snowman!")
# Set the background to blue
s.bgcolor("skyblue")

# Create the t (turtle) and set speed
t = turtle.Pen()
t.speed(0) # 1 is the slowest, 10 or 0 is the fastest

# Draw a circle with a center (x, y), radius and colour
def draw_circle(x, y, radius, pen_color, fill_color):
    # Set the t to a colour
    t.color(pen_color)
    # Fill in what we draw
    t.fillcolor(fill_color)
    t.begin_fill()

    # Move without drawing
    t.penup()

    # Move and start drawing
    t.setposition(x, y)
    t.pendown()

    # Draw a circle with radius 150 and fill it
    t.circle(radius)

    t.end_fill()


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
t.color("orange")
t.fillcolor("orange")
t.penup()
t.setposition(0, 105)
t.begin_fill()
t.pendown()
t.right(150)
t.forward(30)
t.left(150)
t.forward(30)
t.goto(0, 105)
t.end_fill()

# Hat
t.color("black")
t.fillcolor("black")
t.begin_fill()
t.penup()
t.pensize(5)
t.setposition(0, 150)
t.pendown()
t.forward(75)
t.left(90)
t.forward(10)
t.left(90)
t.forward(40)
t.right(90)
t.forward(60)
t.left(90)
t.forward(70)
t.left(90)
t.forward(60)
t.right(90)
t.forward(40)
t.left(90)
t.forward(10)
t.left(90)
t.goto(0, 150)
t.end_fill()
# Ribbon
t.color("red")
t.fillcolor("red")
t.begin_fill()
t.penup()
t.setposition(1, 165)
t.pendown()
t.forward(34)
t.left(90)
t.forward(10)
t.left(90)
t.forward(70)
t.left(90)
t.forward(10)
t.setposition(1, 165)
t.end_fill()

# Arms
def draw_arm(x, y, pen_color):
    t.color(pen_color)
    t.pensize(7)
    t.penup()
    t.setposition(x, y)
    t.pendown()
    t.left(115)
    t.forward(100)
    t.left(45)
    t.forward(30)
    t.right(180)
    t.forward(30)
    t.left(90)
    t.forward(30)
    t.left(180)
    t.forward(30)
    t.right(130)
    t.forward(30)

# Right arm
draw_arm(70, -40, "chocolate")
# Left arm
draw_arm(-70, -40, "chocolate")

# Keep the window ot when done drawing
turtle.done()
