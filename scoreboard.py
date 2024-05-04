from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 180)
        self.write(self.l_score, align='center', font=('Courier', 80, 'bold'))
        self.goto(100, 180)
        self.write(self.r_score, align='center', font=('Courier', 80, 'bold'))

    def l_increment(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_increment(self):
        self.r_score += 1
        self.update_scoreboard()
