import turtle
from turtle import *
import random

ALIGN = "center"
FONT = ("Arial", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.score = 0
        self.write(f"Score:{self.score}", align=ALIGN, font=FONT)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score:{self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align=ALIGN, font=FONT)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()