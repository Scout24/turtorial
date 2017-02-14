#!/usr/bin/env python2
# Future imports must be the first thing in your files.
# Importing division from the future makes "/" behave as in Python3, i.e. it
# produces floats, not integers. Python3 ignores the statement.
from __future__ import division

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
# Draw a heptagon (works with Python 2 due to __future__ import)
draw_polygon(sides=7)
raw_input()
