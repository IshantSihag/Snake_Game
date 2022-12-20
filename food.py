from turtle import Turtle, Screen
from random import randint
class Food:
    def __init__(self):
        self.food=Turtle()
        self.food.penup()
        self.food.shape('circle')
        self.food.color('red')
        self.food.speed('fastest')
        self.food.goto(20*randint(-14, 14),20*randint(-14, 14))
        
    def new(self):
        self.food.goto(20*randint(-14, 14),20*randint(-14, 14))