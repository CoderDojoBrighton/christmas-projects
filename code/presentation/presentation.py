import christmas_tree
import turtle

width = 500
height = 500
s = turtle.Screen()
s.setup(width, height)
s.title("Christmas Tree!")

while True:
    s.clear()
    christmas_tree.draw()

turtle.mainloop()
