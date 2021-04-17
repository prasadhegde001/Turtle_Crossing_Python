from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.score = 0
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 20, "normal"))
        self.score += 1

    def total_score(self):
        self.goto(0, 0)
        self.write(f"Your Total Score: {self.score}", align="center", font=("Courier", 20, "normal"))
