from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.pos = position
        self.create_paddle()

    def create_paddle(self):
        self.shape('square')
        self.shapesize(5, 1)
        self.color('violet')
        self.penup()
        self.goto(self.pos)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
