from turtle import Turtle


class CPUBat(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.goto(680, 0)
        self.shape('square')
        self.shapesize(stretch_len=5)
        self.tilt(90)

    def chase_ball(self, ball):
        if ball.xcor() > 150:
            if ball.ycor() > self.ycor():
                self.sety(self.ycor() + 15)
            if ball.ycor() < self.ycor():
                self.sety(self.ycor() - 15)

    def ball_miss(self, ball):
        if ball.xcor() > 660 and self.distance(ball.pos()) > 60:
            return True
        elif ball.xcor() < -660 and self.distance(ball.pos()) > 60:
            return True
        else:
            return False

