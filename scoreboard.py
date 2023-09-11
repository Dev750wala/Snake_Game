from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("yellow")
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.goto(x=0, y=270)

    def update_score(self):
        self.clear()
        with open("high_score.txt") as high_score_text:
            self.high_score = high_score_text.read()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score

        with open("high_score.txt", mode='w') as update_high_score:
            update_high_score.write(f"{self.high_score}")

        self.score = 0
        self.update_score()

    def count_score(self):
        self.score += 1
        self.update_score()

