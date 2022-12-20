from turtle import Turtle, Screen

class Score:
    def __init__(self):
        self.value = 0
        self.score=Turtle()
        self.score.hideturtle()
        self.score.penup()
        self.score.color('white')
        self.score.goto(0,260)
        self.score.write(f"Score : {self.value}", align = 'center', font=("Calibri", 30, 'normal'))
    
    def increase(self):
        self.value+=1
        self.score.clear()
        self.score.write(f"Score : {self.value}", align = 'center', font=("Calibri", 30, 'normal'))
    
    def over(self):
        self.score.goto(0,-20)
        self.score.write("Game Over", align = 'center', font=("Calibri", 50, 'bold'))
