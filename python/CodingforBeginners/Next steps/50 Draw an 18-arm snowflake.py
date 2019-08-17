#This program creates a snowflake with 18 arms, using the code at the bottom of page 50 to modify the program starting on page 48.
#If you take the # away from the hideturtle line, the turtle will be invisible.


from turtle import *

#set up the turtle
shape("turtle")
speed(10)
pencolor("white")
pensize(6)
#hideturtle

#set up the backdrop
Screen().bgcolor("turquoise")

#create a v shape to repeat
def vshape():
    right(25)
    forward(50)
    backward(50)
    left(50)
    forward(50)
    backward(50)
    right(25)


#use those Vs to create a single arm of a snowflake

def snowflakeArm():
    for x in range(0,4):
        forward(30)
        vshape()
    backward(120)


#function using a for loop to repeat snowflake arm x 6

def snowflake():
    for x in range(0,18):
        snowflakeArm()
        right(20)

snowflake()
