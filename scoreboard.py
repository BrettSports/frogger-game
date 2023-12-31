from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.color("black")
        self.penup()
        self.goto(-230, 260)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Level: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(arg="YOU DIED, LOL!", align=ALIGNMENT, font=FONT)