from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("yellow")
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.goto(x=0, y=270)
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_is_over(self):
        self.goto(0, 0)
        self.color("White")
        self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def count_score(self):
        self.score += 1
        self.clear()
        self.update_score()

