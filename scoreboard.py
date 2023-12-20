from turtle import Turtle

ALIGN = "center"
FONT = ("Courier",18,"normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("White")
        #self.show_score()
        self.get_score_from_file()

    def add_points(self):
        self.score = self.score + 1

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.high_score}", align=ALIGN, font=FONT)

    def gameover(self):
        self.goto(0,245)
        self.write("Game Over", align=ALIGN, font=FONT)

    def refresh_points(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.show_score()
        with open(r"C:\Users\shbs0722\Desktop\python\Snake-main\score_sheet.txt", mode="w") as file:
            file.write(str(self.high_score))
    
    def get_score_from_file(self):
        with open(r"C:\Users\shbs0722\Desktop\python\Snake-main\score_sheet.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.show_score()

