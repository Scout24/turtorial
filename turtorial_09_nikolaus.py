#!/usr/bin/env python2
import turtle

def hvn(size=100):
    """Draw Das Haus vom Nikolaus"""
    diagonal = (2 * size**2) ** .5
    # bottom + diagonal + roof
    turtle.forward(size)
    turtle.left(135)
    turtle.forward(diagonal)
    turtle.right(90)
    turtle.forward(diagonal / 2)
    turtle.right(90)
    turtle.forward(diagonal / 2)
    turtle.right(90)
    # diagonal + left wall + upper part + right wall
    turtle.forward(diagonal)
    turtle.right(135)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)


turtle.delay(100)
hdn()
raw_input()
