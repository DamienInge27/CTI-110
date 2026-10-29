# Damien Inge
# 10/29/2026
# P4 Lab 1
# Use turtle and loops to draw a square and a triangle.

# Import the library
import turtle

# Create the turtle window and drawing object
win = turtle.Screen()
win.bgcolor("teal")
pen = turtle.Turtle()

# Set turtle options
pen.pensize(7)
pen.pencolor("pink")
pen.shape("arrow")

# Code to draw shapes
for side in range(4) :
    pen.forward(250)
    pen.left(90)

# While loop that executes 3 times
sides = 3

pen.penup()
pen.goto(0, 250)
pen.pendown()

while sides > 0:
    pen.forward(250)
    pen.left(120)
    sides = sides - 1

# Keep window open
win.mainloop()