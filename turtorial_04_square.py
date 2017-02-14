#!/usr/bin/env python2
"""A version of turtorial_03_square.py that flake8 and pylint like"""
import turtle


def draw_square(size=100):
    """Draw a square, default size is 100."""
    for _ in range(4):
        # Disable error checking for a single statement:
        turtle.forward(size) # pylint: disable=E1101

        # Disable error checking for entire block.
        # pylint: disable=E1101
        turtle.left(90)


draw_square()
raw_input()
