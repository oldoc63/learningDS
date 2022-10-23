from turtle import *

shape('turtle')
speed(0.5)

def square(sidelength=100):
    for i in range(4):
        forward(sidelength)
        right(90)

def triangle(sidelength=100):
    for i in range(3):
        forward(sidelength)
        right(120)

def polygon(sides, sidelength=100):
    for i in range(sides):
        forward(sidelength)
        right(360/sides)

def squareCircle():
    '''Draws a circle of squares'''
    for i in range(90):
        square(200)
        right(5)

def star(sidelength=200):
    for i in range(5):
        forward(sidelength)
        right(144)

def starSpiral():
    length = 5
    for i in range(90):
        star(length)
        length += 5
        rt(5)

starSpiral()