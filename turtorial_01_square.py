#!/usr/bin/env python2
import turtle

# Draw a square
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)

# When the program terminates, turtle closes the window and our square will
# disappear. raw_input() waits for the user to enter something and press
# ENTER, so we get to see the square. In Python3, use input() instead.
raw_input()
