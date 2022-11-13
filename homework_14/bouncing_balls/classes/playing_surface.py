"""Base class playing surface"""
import turtle
from turtle import Turtle

class PlayingSurface(Turtle):
    """Surface class"""
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        Turtle.__init__(self)
        self.window = turtle.Screen()
        self.window.setup(SCREEN_WIDTH*2, SCREEN_HEIGHT*2)
        self.window.title('Bouncing balls')
        self.window.bgcolor('white')
        self.border = turtle.Turtle()
        self.border.hideturtle()
        self.border.speed(0)
        self.border.pensize(1)
        self.border.color('black')
        self.border.up()
        self.border.goto(-SCREEN_WIDTH, SCREEN_HEIGHT)
        self.border.down()
        self.border.goto(-SCREEN_WIDTH, -SCREEN_HEIGHT)
        self.border.goto(SCREEN_WIDTH, -SCREEN_HEIGHT)
        self.border.goto(SCREEN_WIDTH, SCREEN_HEIGHT)

