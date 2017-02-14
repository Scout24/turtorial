#!/usr/bin/env python2
import turtle

# Draw a polygon, default is a square of size 100.
def draw_polygon(length=100, sides=4):
    for side in range(sides):
        turtle.forward(length)
        turtle.left(360 / sides)

# Default values.
draw_polygon()
# A small triangle
draw_polygon(length=50, sides=3)
# Draw a heptagon (looks ugly with Python 2)
draw_polygon(sides=7)
raw_input()
