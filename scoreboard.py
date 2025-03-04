from turtle import Turtle

ALIGNMENT="center"
FONT=('Arial', 18, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.sety(270)
        self.hideturtle()
        self.color("white")
        self.render_score()

    def render_score(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER!", align=ALIGNMENT, font=FONT)

    def increase_score(self):
            self.score += 1
            self.clear()
            self.render_score()
