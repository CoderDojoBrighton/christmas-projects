---
weight: 1
bookFlatSection: false
title: "Snowman"
---

## Python Snowman

Turtle graphics is a library in Python which can be used for drawing!
You can imagine the turtle as a pen that you can move around the screen and draw with.

To start, we need to load the library using `import`:
```py
import turtle
```


## Setting Up the Screen

We need to set up the idth and height of the screen to draw on.
We can save these values as a *variable* so that it is easy to understand your code
{{% hint info %}}
**What is a variable?**

A variable is a way to store information in a computer program.
You can imagine it as a box with a label on it.
The box stores something, and you refer to it by name on the label.

In the below example, the label is `width`, and the contents is `500`.
{{% /hint %}}

```py
width = 500
height = 500
```

Now we know the width and height, let's create the screen.
We will store the screen in the variable `s`, so we can set the width, height and title.
```py
s = turtle.Screen()
```

To setup the screen, we can use the `s.setup()` function.
{{% hint info %}}
**What is a function?**

A function calls a piece of code written somewhere else.
You can pass values inside brackets called *parameters*, which the code can use.

Certain variables, like your screen `s`, have functions written by other people that we can use.
To use them, add a dot (`.`) after the variable, like below:
{{% /hint %}}
```py
s.setup(width, height)
```

We can also add a title to your window!
```py
s.title("Snowman!")
```

We can also make the background colour blue, like the sky:
```py
s.bgcolor("skyblue")
```

When you run your program, you should see a window on your screen.
![Window](/christmas-projects/snowman/window.png)

Now lets create a turtle to draw with!
```py
t = turtle.Pen()
```

We can set the speed of the turtle of a value between 1 and 10.
1 is the slowest, 10 is the fastest

```py
t.speed(2)
```

Finally, to keep the window open, we will need to call a function call `mainloop` from the `turtle` library.

{{% hint info %}}
**Note**:
Python will execute your code from top to bottom, so keep this line at the bottom of your file so that it is the last thing to run!
{{% /hint %}}

```py
turtle.mainloop()
```

Great!
We're ready to draw

So far, your code should look like this:
```py
import turtle 

# Set up screen
width = 500
height = 500
s = turtle.Screen()
s.setup(width, height)
s.title("Snowman!")
s.bgcolor("skyblue")

# Create turtle
t = turtle.Pen()
t.speed(2)

# Keep the window open
turtle.mainloop()
```

{{% hint info %}}
**Optional but highly recommended:**
It is useful to divide sections of your project with comments as you go along.
This makes it easier to refer back to them later to fix mistakes or change something.
Comments are ignored by the computer so they won't affect your project 

To add a comment, simply add a `#` before some text, such as:
```py
# this is a comment
t = turtle.Pen() # Create the turtle
```
{{% /hint %}}

## Base of the Snowman
We are ready to create the first circle that will be the base of our snowman!
In this step, we will go through each line in detail to explain what the code is doing.

In future steps, we won't need to do this as we will re-use this code.

First, let's tell our turtle what colour the pen should be:
```py
t.color("white")
```

Next, our turtle needs to know what colour to fill in our circle:
```py
t.fillcolor("white")
```

Let's tell our turtle where to begin filling.
This is important because we only want to colour-in certain areas:
```py
t.begin_fill()
```

This next line tells the turtle to lift up the pen before we are ready.
Just think how messy it would get if the pen stayed down before we had arrived where we wanted to draw!
```py
t.penup()
```

Here is where we tell the turtle which position to go to with an `x` and `y` position on the screen:
```py
t.setposition(0, -395)
```

Then we tell the turtle to put the pen back down on the page as we are ready to draw:
```py
t.pendown()
```

Here is where we tell our turtle to draw the circle, the number that we input here is the radius of the circle:
```py
t.circle(150)
```

Last but not least, we tell the turtle to stop filling in the shape:
```py
t.end_fill()
```

**Congratulations!**
Your turtle should draw the base of the snowman!
![Base](/christmas-projects/snowman/base.png)

## The Power of Functions

The complete code can be viewed [here](https://github.com/coderDojoBrighton/christmas-projects/blob/main/code/snowman.py)

