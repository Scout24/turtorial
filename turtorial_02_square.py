#!/usr/bin/env python2
import turtle

# Draw a square, default size is 100.
def draw_square(size=100):
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)

# Use default value:
draw_square()
# Pass own value as argument:
draw_square(123)
# Pass own value as keyword argument:
draw_square(150)


raw_input()
