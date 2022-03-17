from turtle import *
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.7, 0.7)
        self.color("orange")
        self.speed(0)
        random_x = random.randint(-250, +250)
        random_y = random.randint(-250, +250)
        self.goto(random_x, random_y)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-250, +250)
        random_y = random.randint(-250, +250)
        self.goto(random_x, random_y)
