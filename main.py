from turtle import Screen
from screen import Net, Score
from ball import Ball
from user_bat import UserBat
from computerbat import CPUBat
import time


USER_SCOREBOARD_FONT = ('techno', 100, 'bold')
COMPUTER_SCOREBOARD_FONT = ('techno', 100, 'bold')
USER_STARTING_SCORE = 0
COMPUTER_STARTING_SCORE = 0
USER_SCORE_ALIGNMENT = (-100, 300)
COMPUTER_SCORE_ALIGNMENT = (100, 300)
WINNING_SCORE = 5


screen = Screen()
screen.bgcolor('black')
screen.tracer(0)
prompt = screen.textinput(title='Pong', prompt='Begin Game? ').lower()
screen.listen()

if prompt == 'y':
    game_continue = True
else:
    game_continue = False

if game_continue:
    user_bat = UserBat()
    CPU_bat = CPUBat()
    net = Net()
    ball = Ball()
    user_scoreboard = Score(USER_STARTING_SCORE, USER_SCORE_ALIGNMENT, USER_SCOREBOARD_FONT)
    computer_scoreboard = Score(COMPUTER_STARTING_SCORE, COMPUTER_SCORE_ALIGNMENT, COMPUTER_SCOREBOARD_FONT)

while game_continue:
    ball.reset_speed()
    ball.initial_bounce()
    round_not_over = True
    while round_not_over:
        if ball.xcor() > 660:
            if CPU_bat.ball_miss(ball):
                user_scoreboard.increase_score()
                user_scoreboard.refresh(user_scoreboard.score, USER_SCOREBOARD_FONT)
                round_not_over = False
            else:
                ball.increase_speed()
                ball.move(ball.speed)
        elif ball.xcor() < -660:
            if user_bat.ball_miss(ball):
                computer_scoreboard.increase_score()
                computer_scoreboard.refresh(computer_scoreboard.score, COMPUTER_SCOREBOARD_FONT)
                round_not_over = False
            else:
                ball.increase_speed()
                ball.move(ball.speed)
        else:
            ball.move(ball.speed)
            screen.onkeypress(fun=user_bat.up, key='Up')
            screen.onkeypress(fun=user_bat.down, key='Down')
            CPU_bat.chase_ball(ball)

        time.sleep(.015)
        screen.update()

    if user_scoreboard.score == WINNING_SCORE or computer_scoreboard.score == WINNING_SCORE:
        game_continue = False


screen.exitonclick()
