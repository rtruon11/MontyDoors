#Richard Truong
#Compsci 121
#2/01/18
# change bg color when mouse is clicked

import turtle # import graphic library

t1 = turtle.Turtle()
screen = turtle.Screen()

def change (x, y): # call this 'function' when mouse click
    if y > 0 and x > 0:
        screen.bgcolor('blue')
    elif y < 0 and x > 0:
        screen.bgcolor('green')
    elif y > 0 and x < 0:
        screen.bgcolor('yellow')
    else:
        screen.bgcolor('red')

screen.onclick(change)

#Richard_Truong.color('black','blue')
#Richard_Truong.begin_fill
#Richard_Truong.end_fill
