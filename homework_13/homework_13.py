"""Solar system simulation"""
import random
from turtle import *
from math import *


class Planet(Turtle):
    def __init__(self, planet_size, planet_color, radius, star, increase_angle, name='star'):
        Turtle.__init__(self, shape='circle')
        self.name = name
        self.speed(0)
        self.shapesize(*planet_size)
        self.x = 0
        self.y = 0
        self.color(planet_color)
        self.up()
        self.angle = 0
        self.increase_angle = increase_angle
        self.radius = radius
        self.star = star

    def move(self):
        self.x = self.radius * cos(self.angle)
        self.y = self.radius * sin(self.angle)
        self.goto(self.star.xcor() + self.x, self.star.ycor() + self.y)
        self.angle += self.increase_angle


class Asteroid(Turtle):
    def __init__(self, planet_size, planet_color, radius, star, angle, name='star'):
        Turtle.__init__(self, shape='circle')
        self.name = name
        self.speed(0)
        self.shapesize(*planet_size)
        self.x = 0
        self.y = 0
        self.color(planet_color)
        self.up()
        self.angle = angle
        self.radius = radius
        self.star = star

    def move(self):
        self.x = self.radius * cos(self.angle)
        self.y = self.radius * sin(self.angle)
        self.goto(self.star.xcor() + self.x, self.star.ycor() + self.y)
        self.angle = self.angle


def asteroid_position(rings_number: int, asteroid_number: int):
    asteroid_distance = []
    asteroid_angle = []
    asteroid_position = {}
    for distance in range(rings_number):
        asteroid_distance.append(random.randrange(160, 210, 10))
    counter = 0
    while counter <= len(asteroid_distance) - 1:
        for angle in range(asteroid_number):
            asteroid_angle.append(random.randrange(0, 360))
        asteroid_position[asteroid_distance[counter]] = asteroid_angle
        counter += 1
        asteroid_angle = []
    return asteroid_position.items()


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

window = Screen()
window.bgcolor('black')
window.title('Solar system')
window.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
window.onkey(window.bye, 'Escape')

sun = Turtle(shape='circle')
sun.color('#d9631a')
sun.shapesize(3, 3)


for distance, corner in asteroid_position(4, 50):
    for asteroid in corner:
        sky_object = Asteroid((0.1, 0.1), 'white', distance, sun, asteroid)
        sky_object.move()

mercury = Planet((0.2, 0.2), 'gray', 40, sun, 0.047)

venus = Planet((0.6, 0.6), 'yellow', 50, sun, 0.035)

earth = Planet((1, 1), '#2845d4', 74, sun, 0.03)
moon = Planet((0.4, 0.4), 'gray', 17, earth, 0.001)

mars = Planet((0.5, 0.5), '#de4318', 114, sun, 0.024)
fobos = Planet((0.2, 0.2), 'gray', 10, mars, 0.003)
deimos = Planet((0.2, 0.2), 'gray', 15, mars, 0.0014)

jupiter = Planet((3.4, 3.4), '#19a8e6', 289, sun, 0.013)

sat_ring = Planet((5.5, 5.5), 'white', 400, sun, 0.01)
sat_ring_black = Planet((3.9, 3.9), 'black', 400, sun, 0.01)
saturn = Planet((2.5, 2.5), '#454c4f', 400, sun, 0.01)

window.listen()

while True:
    mercury.move()

    venus.move()

    earth.move()
    moon.move()

    mars.move()
    fobos.move()
    deimos.move()

    jupiter.move()

    sat_ring.move()
    sat_ring_black.move()
    saturn.move()


