#This is a variant of the snowstorm program that varies the code in step 2 on page 53.
#This means each snowflake is a single colour.


from turtle import *
import random


shape("turtle")
speed(10)
width(6)

Screen().bgcolor("turquoise")

colours = ["blue", "purple", "cyan", "white", "yellow", "green", "orange"]


def vshape(size):
    right(25)
    forward(size)
    backward(size)
    left(50)
    forward(size)
    backward(size)
    right(25)

def snowflakeArm(size):
    for x in range(0,4):
        forward(size)
        vshape(size)
    backward(size*4)

def snowflake(size):
    color(random.choice(colours))
    for x in range(0,6):
        snowflakeArm(size)
        right(60)
        #color(random.choice(colours))

for i in range(0,10):
    size= random.randint(5,30)
    x=random.randint(-400,400)
    y=random.randint(-400,400)
    penup()
    goto(x,y)
    pendown()
    snowflake(size)
    
snowflake(size)
