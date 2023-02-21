from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 280)
        self.color("white")
        self.write(f"Score: {self.score}", align="center", font=("Arial,24,normal"))
        self.hideturtle()

    def update(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial,24,normal"))

    def gameover(self):
        self.goto(0, 0)
        self.write("Game-over", align="center", font=("Arial,24,normal"))
