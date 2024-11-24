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



The complete code can be viewed [here](https://github.com/coderDojoBrighton/christmas-projects/blob/main/code/snowman.py)

