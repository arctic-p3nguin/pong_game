from turtle import Turtle
import time
import random
import pygame

DELTA_TIME = 0.02
pygame.init()
hit = pygame.mixer.Sound("sh_pickup03.mp3")


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.shape("square")
        self.setheading(0)
        self.shapesize(0.7, 0.7, 1)
        self.color("white")
        self.penup()
        self.delta_x = 0
        self.delta_y = 0

    def move(self):
        self.goto(self.xcor()+self.delta_x, self.ycor()+self.delta_y)
        time.sleep(DELTA_TIME)

    def serve_left(self):
        self.setposition(0, 0)
        time.sleep(1)
        self.delta_x = -20
        self.delta_y = random.randint(-20, -10)

    def serve_right(self):
        self.setposition(0, 0)
        time.sleep(1)
        self.delta_x = 20
        self.delta_y = random.randint(10, 20)

    def head_bounce(self):
        self.delta_y *= -1
        hit.play()

    def bottom_bounce(self):
        self.delta_y *= -1
        hit.play()

    def paddle_bounce(self):
        self.delta_y += random.randint(-5, 5)
        self.delta_x *= -1
        hit.play()




