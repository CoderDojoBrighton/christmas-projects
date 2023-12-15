import christmas_tree, title, snowflake, wreath, lights
import turtle

speed = 5
width = 500
height = 500
s = turtle.Screen()
s.setup(width, height)
s.title("CodeDojo Christmas")


while True:
    s.clear()
    title.draw(speed)
    wreath.draw()
    snowflake.draw(900, 200)
    snowflake.draw(400, -80)
    snowflake.draw(800, 20)
    snowflake.draw(800, -40)
    snowflake.draw(800, 160)
    snowflake.draw(750, 230)
    christmas_tree.draw(speed, -600)
    christmas_tree.draw(speed, 550)
    lights.draw(speed, -600, 550)

turtle.mainloop()
