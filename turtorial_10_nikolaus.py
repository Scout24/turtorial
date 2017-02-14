#!/usr/bin/env python2
import turtle

def draw_square(size=100):
    for x in range(4):
        turtle.forward(size)
        turtle.left(90)

def hdn(size=100):
    """Draw Das Haus des Nikolaus, using draw_square()"""
    half_diagonal = (2 * size**2) ** .5 / 2

    draw_square(size)
    # Draw a "fish".
    turtle.left(45)
    turtle.forward(half_diagonal)
    draw_square(size=half_diagonal)
    turtle.right(90)
    turtle.forward(half_diagonal)


turtle.delay(100)
hdn()
raw_input()
