import christmas_tree, title, snowflake
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
    # snowflake.draw(speed+2, 210)
    snowflake.draw(600, 190)
    snowflake.draw(400, -80)
    snowflake.draw(600, 30)
    snowflake.draw(800, -40)
    snowflake.draw(800, 160)
    snowflake.draw(900, -10)
    snowflake.draw(300, 130)
    snowflake.draw(750, 230)
    christmas_tree.draw(speed)

turtle.mainloop()
