#!/usr/bin/env python2
from __future__ import division

import turtle

def draw_polygon(length=100, sides=4):
    for side in range(sides):
        turtle.forward(length)
        turtle.left(360 / sides)
        if length > 10 and sides > 3:
            draw_polygon(length=length / 3, sides=sides - 1)

# Default values.
draw_polygon(length=250, sides=5)
raw_input()
