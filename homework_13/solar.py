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


SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 950


window = Screen()
window.bgcolor('black')
window.title('Solar system')
window.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
window.onkey(window.bye, 'Escape')

sun = Turtle(shape='circle')
sun.color('#d9631a')
sun.shapesize(5, 5)

mercury = Planet((0.2, 0.2), 'grey', 80, sun, 0.047)
venus = Planet((0.3, 0.3), 'orange', 100, sun, 0.035)
earth = Planet((0.5, 0.5), 'blue', 140, sun, 0.030)
moon = Planet((0.2, 0.2), 'grey', 15, earth, -0.05)
mars = Planet((0.4, 0.4), 'red', 170, sun, 0.024)
fobos = Planet((0.08, 0.08), 'grey', 10, mars, 0.02)
demos = Planet((0.07, 0.07), 'grey', 15, mars, -0.02)
Jupiter = Planet((1.5, 1.5), 'brown', 210, sun, 0.013)
saturn = Planet((1.3, 1.3), 'yellow', 250, sun, 0.0097)


ring1 = Planet((0.1, 0.1), 'white', 23, saturn, 0.02)
ring2 = Planet((0.1, 0.1), 'white', 23, saturn, 0.03)
ring3 = Planet((0.1, 0.1), 'white', 23, saturn, 0.04)
ring4 = Planet((0.1, 0.1), 'grey', 23, saturn, 0.05)
ring5 = Planet((0.1, 0.1), 'white', 23, saturn, 0.06)
ring6 = Planet((0.1, 0.1), 'white', 23, saturn, 0.07)
ring7 = Planet((0.1, 0.1), 'grey', 23, saturn, 0.08)
ring8 = Planet((0.1, 0.1), 'white', 23, saturn, -0.08)
ring9 = Planet((0.1, 0.1), 'white', 23, saturn, -0.07)
ring10 = Planet((0.1, 0.1), 'white', 23, saturn, -0.06)
ring11 = Planet((0.1, 0.1), 'grey', 23, saturn, -0.05)
ring12 = Planet((0.1, 0.1), 'white', 23, saturn, -0.04)
ring13 = Planet((0.1, 0.1), 'white', 23, saturn, -0.03)
ring14 = Planet((0.1, 0.1), 'white', 23, saturn, -0.02)
ring15 = Planet((0.1, 0.1), 'white', 23, saturn, -0.01)


uranus = Planet((0.9, 0.9), 'light blue', 300, sun, 0.0068)
neptune = Planet((0.8, 0.8), 'dark blue', 350, sun, 0.0054)
pluton = Planet((0.3, 0.3), 'blue', 400, sun, 0.0047)


window.listen()

while True:
    mercury.move()
    venus.move()
    earth.move()
    moon.move()
    mars.move()
    fobos.move()
    demos.move()
    Jupiter.move()
    saturn.move()
    ring1.move()
    ring2.move()
    ring3.move()
    ring4.move()
    ring5.move()
    ring6.move()
    ring7.move()
    ring8.move()
    ring9.move()
    ring10.move()
    ring11.move()
    ring12.move()
    ring13.move()
    ring14.move()
    ring15.move()
    uranus.move()
    neptune.move()
    pluton.move()
