from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.points = 0
        self.hideturtle()
        self.goto(0, 250)
        self.color("white")
        self.score_refresh()

    def score_refresh(self):
        self.points += 1
        self.clear()
        self.write(f"SCORE: {self.points}", False, "center", font=("Arial", 15, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", False, "center", font=("Arial", 15, "normal"))
