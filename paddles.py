from turtle import Turtle

X = [-380, 372]


class Paddles(Turtle):

    def __init__(self, position):
        super().__init__()

        self.generate_paddle(position)

    def generate_paddle(self, position):
        self.setheading(270)
        self.shape("square")
        self.shapesize(1, 5)
        self.penup()
        self.speed("fastest")
        self.goto(position)
        self.color("white")

    def go_up(self):
        if self.ycor() <= 250:
            new_y = self.ycor() + 40
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() >= -250:
            new_y = self.ycor() - 40
            self.goto(self.xcor(), new_y)





