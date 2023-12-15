import christmas_tree, title
import turtle

width = 500
height = 500
s = turtle.Screen()
s.setup(width, height)
s.title("Christmas Tree!")

speed = 2
while True:
    s.clear()
    title.draw(speed)
    christmas_tree.draw(speed)

turtle.mainloop()
