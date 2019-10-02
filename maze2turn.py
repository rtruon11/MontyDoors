# Name: Richard Truong rxt5171@psu.edu
# CMPSC 121 HW 3
# Date: 03/03/2018
# Title: maze2turn
# Description: driver car maze simulation

import turtle

car = turtle.Turtle()
screen = turtle.Screen()

def drawMaze():
    car.speed(0)
    car.penup()# innner middle up
    car.setpos(-100,70)
    car.pendown()
    car.left(90)
    car.forward(110)

    car.penup()# left outer side up
    car.setpos(-200,0)
    car.setheading(0)
    car.pendown()
    car.left(90)
    car.forward(180)
    
    car.penup()# bottom middle down
    car.setpos(-200,0)
    car.setheading(0)
    car.pendown()
    car.forward(200)
    car.right(90)
    car.forward(60)

    car.penup()# top middle down
    car.setpos(-100,70)
    car.setheading(0)
    car.pendown()
    car.forward(200)
    car.right(90)
    car.forward(130)

def onPath():
    x = car.xcor()
    y = car.ycor()
    if 0 < x < 100 and -60 < y < 70:
        return 1

    if -200 < x < 100 and 0 < y < 70:
        return 1
    
    if -200 < x < -100 and 0 < y < 180:
        return 1

    else:
        return 0

def initializeCar():
    car.penup()
    car.setpos(50,-50)
    car.pendown()
    car.setheading(90)
    car.pencolor('blue')

def fwd():
    car.forward(10)
    if onPath()==0:
        screen.bgpic ('irs.gif')
        screen.bgcolor('red')
        car.pencolor('red')

    x = car.xcor()
    y = car.ycor()
    if -200 < x < -100 and y > 180:
        screen.bgpic ('money.gif')
        screen.bgcolor('green')
        car.pencolor('green')

def left():
    car.left(10)
    
def right():
    car.right(10)

screen.onkey(fwd, 'Up')
screen.onkey(left, 'Left')
screen.onkey(right, 'Right')

screen.listen()

drawMaze()

#position car at start position and angle

initializeCar()
