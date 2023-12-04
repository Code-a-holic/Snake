from turtle import Turtle

ALIGN = "center"
FONT = ("Courier",18,"normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("White")
        self.show_score()

    def add_points(self):
        self.score = self.score + 1

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def gameover(self):
        self.goto(0,245)
        self.write("Game Over", align=ALIGN, font=FONT)