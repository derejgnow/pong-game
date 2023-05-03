from computerbat import CPUBat


class UserBat(CPUBat):
    def __init__(self):
        super().__init__()
        self.goto(-690, 0)

    def up(self):
        self.sety(self.ycor() + 50)

    def down(self):
        self.sety(self.ycor() - 50)


