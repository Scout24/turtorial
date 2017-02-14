#!/usr/bin/env python2
import turtle

# Draw a square, default size is 100.
def draw_square(size=100):
    for x in range(4):
        turtle.forward(size)
        turtle.left(90)


draw_square()
raw_input()
