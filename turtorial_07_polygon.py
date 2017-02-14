#!/usr/bin/env python2
from __future__ import division
import turtle


def draw_polygon(length=100, sides=4):
    for side in range(sides):
        turtle.forward(length)
        turtle.left(360 / sides)


# Convenience functions that use draw_polygon().
def draw_triangle(length=100):
    draw_polygon(length=length, sides=3)


def draw_square(length=100):
    draw_polygon(length=length, sides=4)


# A small triangle
draw_triangle(length=50)
# A large square
draw_square(length=123)


raw_input()
