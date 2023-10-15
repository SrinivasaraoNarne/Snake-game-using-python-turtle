from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 24, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        with open("scoring.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.score = 0
        self.hideturtle()
        self.goto(0, 260)
        self.show()

    def show(self):
        self.clear()
        self.write(f"score: {self.score}, High Score: {self.high_score}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.show()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("scoring.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.show()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGN, font=FONT)

