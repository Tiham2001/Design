from turtle import *
from random import randint
speed(20000000)
bgcolor("black")
x = 1
while x < 1000:
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    colormode(255)
    pencolor(r,g,b)
    fd(50+x)
    rt(90.911)
    x=x+1

def exitonClick():
    pass

exitonClick()
