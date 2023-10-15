from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        ran_x = random.randint(a=-280, b=280)
        ran_y = random.randint(a=-280, b=280)
        self.goto(ran_x, ran_y)
