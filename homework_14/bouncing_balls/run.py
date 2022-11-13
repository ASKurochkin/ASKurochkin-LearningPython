import random

from homework.homework_14.bouncing_balls.classes.playing_surface import PlayingSurface
from homework.homework_14.bouncing_balls.classes.ball import Ball


def make_window(weight, height):
    """Make window and border of surface for our game"""
    PlayingSurface(weight, height)


def make_balls(number_of_balls, shapesize, SCREEN_WIDTH, SCREEN_HEIGHT, speed_bouncing):
    """Create balls that will fall"""
    balls = []
    for ball_number in range(number_of_balls):
        red = random.random()
        green = random.random()
        blue = random.random()
        color = (red, green, blue)
        ball = Ball(color, shapesize, SCREEN_WIDTH, SCREEN_HEIGHT, speed_bouncing)
        balls.append(ball)
    return balls

if __name__ == '__main__':
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 800
    ball_size = 3
    number_of_balls = 7
    speed_bouncing = 0.6

    make_window(SCREEN_WIDTH, SCREEN_HEIGHT)
    balls = make_balls(number_of_balls, ball_size, SCREEN_WIDTH, SCREEN_HEIGHT, speed_bouncing)

    while True:
        for ball in balls:
            ball.move()

    turtle.mainloop()