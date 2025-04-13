from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_a = 0
        self.score_b = 0
        self.pencolor("white")
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.update()

    def update(self):
        self.clear()
        self.goto(-60, 180)
        self.write(self.score_a, align="center", font=("OCR A Std", 44, "normal"))
        self.goto(60, 180)
        self.write(self.score_b, align="center", font=("OCR A Std", 44, "normal"))

    def scored(self, obj):
        # self.score_a += 1
        if obj == 1:
            self.score_a += 1
        else:
            self.score_b += 1
        self.update()


