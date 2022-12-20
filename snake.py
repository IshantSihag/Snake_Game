from turtle import Turtle

INITIAL=[(0,0)]

class Snake:
    def __init__(self):
        self.body=[]
        self.createSnake()
    

    def createSnake(self):
        for i in INITIAL:
            self.intital=Turtle(shape="square")
            self.intital.penup()
            self.intital.color("grey")
            self.intital.goto(i)
            self.body.append(self.intital)

    def grow(self):
        self.new=Turtle(shape="square")
        self.new.penup()
        self.new.color("white")
        self.new.goto(self.body[0].position())
        # self.body[0].forward(20)
        self.body.append(self.new)


    def move(self):
        self.body[-1].goto(self.body[0].xcor(),self.body[0].ycor())
        self.body[0].forward(20)
        self.body.insert(1, self.body[-1])
        self.body=self.body[:-1]

    def left(self):
        if(self.body[0].heading()!=0):
            self.body[0].setheading(180)

    def right(self):
        if(self.body[0].heading()!=180):
            self.body[0].setheading(0)

    def up(self):
        if(self.body[0].heading()!=270):
            self.body[0].setheading(90)

    def down(self):
        if(self.body[0].heading()!=90):   
            self.body[0].setheading(270)