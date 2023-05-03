from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.speed = 20


    def move(self, ball_speed):
        self.bounce()
        self.forward(ball_speed)

    def increase_speed(self):
        self.speed += 5

    def reset_speed(self):
        self.speed = 20

    def initial_bounce(self):
        self.setposition(0, 0)
        initial_movement_angle = random.randrange(120, 240)
        self.setheading(initial_movement_angle)

    def bounce(self):
    # angle of incidence = angle of reflection
        if self.xcor() > 660 or self.xcor() < -660:
        # for ball bouncing off vertical walls
            angle_of_incidence = self.vertical_primary_angle()
            angle_of_reflection = angle_of_incidence
            # ball hitting left wall going downwards
            if self.heading() > 270:
                self.setheading(180 + angle_of_reflection)
            # ball hitting left wall going downwards
            elif self.heading() > 180:
                self.setheading(360 - angle_of_reflection)
            # ball hitting left wall going upwards
            elif self.heading() > 90:
                self.setheading(angle_of_reflection)
            # ball hitting right wall going upwards
            else:
                self.setheading(180 - angle_of_reflection)

        if self.ycor() > 420 or self.ycor() < -420:
        # for ball bouncing off horizontal walls
            angle_of_incidence = self.horizontal_primary_angle()
            angle_of_reflection = angle_of_incidence
            # ball hitting floor going right
            if self.heading() > 270:
                self.setheading(90 - angle_of_reflection)
            # ball hitting floor going left
            elif self.heading() > 180:
                self.setheading(90 + angle_of_reflection)
            # ball hitting ceiling going left
            elif self.heading() > 90:
                self.setheading(270 - angle_of_reflection)
            # ball hitting ceiling going right
            else:
                self.setheading(270 + angle_of_reflection)

    def vertical_primary_angle(self):
        # ball hitting right wall going downwards
        if self.heading() > 270:
            return 90 - (self.heading() - 270)
        # ball hitting left wall going downwards
        elif self.heading() > 180:
            return self.heading() - 180
        # ball hitting left wall going upwards
        elif self.heading() > 90:
            return 180 - self.heading()
        # ball hitting right wall going upwards
        else:
            return self.heading()

    def horizontal_primary_angle(self):
        # ball hitting floor going right
        if self.heading() > 270:
            return self.heading() - 270
        # ball hitting floor going left
        elif self.heading() > 180:
            return 90 - (self.heading() - 180)
        # ball hitting ceiling going left
        elif self.heading() > 90:
            return self.heading() - 90
        # ball hitting ceiling going right
        else:
            return 90 - self.heading()
