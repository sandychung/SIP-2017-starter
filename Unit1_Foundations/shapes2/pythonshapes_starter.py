from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(500,300)
x_pos = -250
y_pos = -150
t.setposition(x_pos, y_pos)

### Write your code below:
sides = 8
x = 360/sides
for i in range(sides):
    t.forward (50)
    t.right (x)



# Close window on click.
exitonclick()
