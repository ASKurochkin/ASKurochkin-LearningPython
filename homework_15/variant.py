"""Game 'Travel Turtle'"""
from turtle import *
from random import random, randint


class Window:
    """Create window for our game"""
    SCREEN_WIDTH = 1080
    SCREEN_HEIGHT = SCREEN_WIDTH // 2
    HALF_WIDTH = SCREEN_WIDTH // 2
    HALF_HEIGHT = SCREEN_HEIGHT // 2

    def __init__(self, screen_title: str = 'Travel turtle'):
        self.field = Screen()
        self.field.title(screen_title)
        self.field.setup(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.field.onkey(self.field.bye, 'Escape')
        self.field.tracer(0)
        self.field.listen()
        self.field.onkeypress(Player().run_turtle_run, 'Up')


class Sprite(Turtle):
    """Base class for creating turtle-object"""
    def __init__(self, shape_name: str):
        super().__init__(shape=shape_name)
        self.hideturtle()
        self.up()


class Player(Sprite):
    """Create a figure of our player and describe its interaction with the game"""
    size = 30

    def __init__(self, player: str = 'turtle'):
        super().__init__(player)
        self.goto(self.get_start_position())
        self.color('green')
        self.tiltangle(90)
        self.showturtle()
        if self.ycor() >= Window.SCREEN_HEIGHT:
            self.goto(self.get_start_position())

    def run_turtle_run(self):
        """Player movement rules"""
        y = self.ycor()
        return self.sety(y+30)

    def repeat(self):
        if self.ycor() >= Window.SCREEN_HEIGHT:
            return self.goto(self.get_start_position())

    @staticmethod
    def get_start_position():
        return 0, (-Window.HALF_HEIGHT + Player.size // 2)


class Game_level(Sprite):
    """Level indicator"""
    def __init__(self, frame: str = 'square'):
        super().__init__(frame)
        self.level = 1
        self.goto(-Window.HALF_WIDTH + 20, Window.HALF_HEIGHT - 60)
        self.frame_level = self.write(f'Level {self.level}', False, font=('Arial', 30, 'bold'))

    def level_up(self):
        if Player().ycor() >= Window().SCREEN_HEIGHT:
            self.level += 1


class Barrier(Sprite):
    """Creating barriers for the player to overcome"""
    def __init__(self, shape_name: str = 'square'):
        super().__init__(shape_name)
        self.color(self.get_random_color())
        self.goto(self.get_random_position())
        self.showturtle()
        self.x = 0
        self.y = 0

    def move(self):
        """Barrier movement rules"""
        self.x = self.xcor()
        self.y = self.ycor()
        self.goto(self.x + 0.05, self.y)


    @staticmethod
    def get_random_color():
        return random(), random(), random()

    @staticmethod
    def get_random_position():
        return randint(-Window.HALF_WIDTH, Window.HALF_HEIGHT*2), \
               randint(-Window.HALF_HEIGHT+(2*Player.size), Window.HALF_HEIGHT)


class Game:
    """Launch and interaction of game elements"""
    __number_of_barriers = 10
    __speed = 0.1

    def __init__(self, difficulty: int, level: float):
        Game.__number_of_barriers = difficulty
        Game.__speed = level
        self.window = Window()
        self.barriers = self.make_barrier(difficulty)

    def run(self):
        """Game launcher"""
        for barrier in self.barriers:
            barrier().move()
        while True:
            Game_level()
            self.window.field.update()

    @staticmethod
    def make_barrier(difficulty: int):
        return [Barrier for _ in range(difficulty)]

if __name__ == '__main__':
    game = Game(difficulty=10, level=0.1)
    game.run()