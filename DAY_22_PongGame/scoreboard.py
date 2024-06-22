from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align='center', font=('Courier', 70, 'bold'))
        self.goto(100, 200)
        self.write(self.r_score, align='center', font=('Courier', 70, 'bold'))

    def score_point(self, paddle_side):
        if paddle_side == 'right':
            self.r_score += 1
        elif paddle_side == 'left':
            self.l_score += 1
        self.update_scoreboard()