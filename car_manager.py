import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager(Turtle):
        def __init__(self):
            super().__init__()
            self.penup()
            self.goto(0, 240)
            self.shape("square")
            self.shapesize(stretch_wid=1, stretch_len=2)
            self.color(random.choice(COLORS))
