from turtle import Turtle


class Net(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.width(5)
        self.penup()
        self.hideturtle()
        self.goto(0, -400)
        for x in range(21):
            self.pendown()
            self.setheading(90)
            self.forward(20)
            self.penup()
            self.forward(20)


class Score(Turtle):
    def __init__(self, score, alignment, font):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.setposition(alignment)
        self.score = score
        self.display_score(self.score, font)

    def display_score(self, score, font):
        self.write(arg=score, align='center', font=font)

    def increase_score(self):
        self.score += 1

    def refresh(self, score, font):
        self.clear()
        self.display_score(score=score, font=font)










