from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import Score
from time import sleep
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake")
screen.bgcolor("#000000")
screen.tracer(0)

game_on=False

startup=Turtle()
startup.hideturtle()
startup.penup()
startup.goto(0,20)
startup.color('red')
startup.write("This is an easy mode", align = 'center', font=("Calibri", 30, 'bold'))
startup.goto(0,-20)
startup.write("You can bite your tail", align = 'center', font=("Comic Sans", 30, 'bold'))
startup.goto(0,-70)
startup.write("Press Space bar to continue", align = 'center', font=("Comic Sans", 20, 'bold'))
# startup.goto(0,-110)
# startup.write("Press Space bar to continue", align = 'center', font=("Comic Sans", 20, 'bold'))
screen.update()
# sleep(1)


snake=Snake()
food=Food()
score=Score()
screen.update()


def start(game_on):
    if (game_on==False):
        startup.clear()
        game_on=True


screen.listen()
screen.onkey(key=' ', fun=start(game_on))
screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)


speed=0.1
while True:
    if (True):
        # sleep(1)   
        screen.update()
        screen.update()
        sleep(speed)
        speed/=1.001
        snake.move()

        if(snake.body[0].distance(food.food)<15):
            screen.update()
            food.new()
            score.increase()
            snake.grow()
            screen.update()

        if(snake.body[0].xcor()>300 or snake.body[0].xcor()<-300):
            score.over()
            game_on=False
            break
        if(snake.body[0].ycor()>300 or snake.body[0].ycor()<-300):
            score.over()
            game_on=False
            break
    # else:
         
screen.exitonclick()

