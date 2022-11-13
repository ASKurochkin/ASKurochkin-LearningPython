"""Base class for balls"""
from turtle import *
import random


class Ball(Turtle):
    """Ball class"""
    def __init__(self, color, shapesize, SCREEN_WIDTH, SCREEN_HEIGHT, speed_bouncing):
        Turtle.__init__(self, shape='circle')
        self.speed_bouncing = speed_bouncing
        self.weight = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.color(color)
        self.shapesize(shapesize)
        self.up()
        self.goto(random.randint(-SCREEN_WIDTH, SCREEN_WIDTH), random.randint(300, SCREEN_HEIGHT))
        self.speed_x = random.randint(-4, 4)
        self.speed_y = 0

    def move(self):
        self.speed_y = self.speed_y - self.speed_bouncing
        self.goto(self.xcor() + self.speed_x, self.ycor() + self.speed_y)
        if self.ycor()-45 <= -self.height:
            self.speed_y = -self.speed_y
        elif self.xcor()+40 >= self.weight or self.xcor()-40 <= -self.weight:
            self.speed_x = -self.speed_x
