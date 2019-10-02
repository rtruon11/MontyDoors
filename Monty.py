# Name: Richard Truong & Aliaksei Kavalchuk
# CMPSC 121 Project 1 Version 2
# Date: 03/20/2018
# Title: montydoorv2
# Description: opening door chance taking geporady

import turtle  # import graphics library
import random  # import random function
from turtle import *  # imports function to do gifs into Turtle

play = turtle.Screen()  # creates the  y,n key selection recognition
key = turtle.Screen()  # creates the  1,2,3 key selection recognition
screen1 = turtle.Screen()
switchcommand = turtle.Screen()  # creates the k,l key selection recognition
screen = turtle.Screen()  # allows user to click onto screen
Richard_Aliaksei = turtle.Turtle()
Play_again = turtle.Turtle()  # play or exit button Turtle drawing box
setup( width=1920, height=1080, startx=0, starty=0)

Richard_Aliaksei.hideturtle()
Richard_Aliaksei.penup()
Richard_Aliaksei.setpos(-50, 0)  # position of text
Richard_Aliaksei.write("Do you want to play? (press y for yes, n for no)", font=('Arial', 16, 'normal'))
time.sleep(3)  # delays next line by 3 second
Richard_Aliaksei.undo()  # erase text

screen.bgpic('Game Stage.gif')

goat_counter = 0
car_counter = 0


def sim():  # definition sim (is called on later)
    Richard_Aliaksei = turtle.Turtle()  # create a turtle object
    Richard_Aliaksei.speed(0)
    Richard_Aliaksei.color("white")
    Richard_Aliaksei.penup()
    Richard_Aliaksei.setpos(-90, 432)
    Richard_Aliaksei.pendown()
    Richard_Aliaksei.begin_fill()
    Richard_Aliaksei.forward(500)
    Richard_Aliaksei.right(90)
    Richard_Aliaksei.forward(100)
    Richard_Aliaksei.right(90)
    Richard_Aliaksei.forward(500)
    Richard_Aliaksei.right(90)
    Richard_Aliaksei.forward(100)
    Richard_Aliaksei.end_fill()
    Richard_Aliaksei.hideturtle()

    Richard_Aliaksei.speed(0)
    key = turtle.Screen()  # ?
    screen = Screen()
    Mascot = 'WawaMascot1.gif'  # Mascot gif
    GameBoard = 'ScoreBoard.gif'  # Scoreboard gif
    CS = 'car.gif'  # name assigned to car gif
    G1 = 'goat.gif'  # name assigned to goat gif
    G2 = 'goat.gif'  # name assigned to goat gif
    G3 = 'goat.gif'  # name assigned to goat gif
    WL = 'WawaLogo.gif'  # name assigned to wawa logo
    screen.register_shape(G1)  # input goat gif into turtle as shape
    screen.register_shape(CS)  # input car gif into turtle as shape
    screen.register_shape(G2)  # input goat gif into turtle as shape
    screen.register_shape(G3)  # input goat gif into turtle as shape
    screen.register_shape(WL)  # input wawa logo into turtle as shape
    screen.register_shape(Mascot)
    screen.register_shape(GameBoard)

    screen.bgcolor('white')  # change background color

    Richard_Aliaksei.penup()
    # set position for doors to be drawn
    Richard_Aliaksei.pendown()
    WawaMascot = Turtle(Mascot)
    WawaMascot.speed(0)
    WawaMascot.penup()
    WawaMascot.setpos(-300, 188)

    ScoreBored = Turtle(GameBoard)
    ScoreBored.speed(0)
    ScoreBored.penup()
    ScoreBored.setpos(-690, 300)

    goat = Turtle(G1)
    goat.speed(0)
    goat.penup()
    goat2 = Turtle(G2)
    goat2.speed(0)
    goat2.penup()
    car = Turtle(CS)
    car.speed(0)
    car.penup()
    wawalogo = Turtle(WL)
    wawalogo.penup()
    wawalogo.setpos(-280, 375)

    i = 0

    imagepositions = [(-130, 200), (20, 200), (170, 200)]  # placement of images x and y coordinates

    def car_win1():
        dtext = turtle.Turtle()
        dtext.penup()
        dtext.setpos(-85, 350)
        dtext.pendown()
        dtext.write("Congradulations! You win a car!", font=('Arial', 12, 'normal'))
        time.sleep(1)
        goat2reveal = Turtle(G3)
        goat2reveal.penup()
        goat2reveal.setpos(goatpos)
        carreveal = Turtle(CS)
        carreveal.penup()
        carreveal.setpos(carpos)
        global car_counter
        car_counter += 1
        print('goat', goat_counter, 'car', car_counter)

    def car_win2():
        dtext = turtle.Turtle()
        dtext.penup()
        dtext.setpos(-85, 350)
        dtext.pendown()
        dtext.write("Congradulations! You win a car!", font=('Arial', 12, 'normal'))
        time.sleep(1)
        goat1reveal = Turtle(G3)
        goat1reveal.penup()
        goat1reveal.setpos(goatpos2)
        carreveal = Turtle(CS)
        carreveal.penup()
        carreveal.setpos(carpos)
        global car_counter
        car_counter += 1
        print('goat', goat_counter, 'car', car_counter)

    def goat_lose1():
        dtext = turtle.Turtle()
        dtext.penup()
        dtext.setpos(-85, 350)
        dtext.pendown()
        dtext.write("Congradulations! You win a goat!", font=('Arial', 12, 'normal'))
        time.sleep(1)
        goat2reveal = Turtle(G3)
        goat2reveal.penup()
        goat2reveal.setpos(goatpos)
        carreveal = Turtle(CS)
        carreveal.penup()
        carreveal.setpos(carpos)
        global goat_counter
        goat_counter += 1
        print('goat', goat_counter, 'car', car_counter)

    def goat_lose2():
        dtext = turtle.Turtle()
        dtext.penup()
        dtext.setpos(-85, 350)
        dtext.pendown()
        dtext.write("Congradulations! You win a goat!", font=('Arial', 12, 'normal'))
        time.sleep(1)
        goat1reveal = Turtle(G3)
        goat1reveal.penup()
        goat1reveal.setpos(goatpos2)
        carreveal = Turtle(CS)
        carreveal.penup()
        carreveal.setpos(carpos)
        global goat_counter
        goat_counter += 1
        print('goat', goat_counter, 'car', car_counter)

    def carwinswitch():
        carwinswitch += 1

    def carwinhold():
        carwinhold += 1

    def doorchoice():
        Richard_Aliaksei.penup()
        Richard_Aliaksei.setpos(-125, 70)
        i = 0
        while i < 3:
            Richard_Aliaksei.begin_fill()
            Richard_Aliaksei.setheading(0)
            Richard_Aliaksei.color("yellow")
            Richard_Aliaksei.pendown()
            Richard_Aliaksei.circle(15)
            Richard_Aliaksei.penup()
            Richard_Aliaksei.forward(150)
            Richard_Aliaksei.end_fill()
            i += 1

    while i in range(1):
        doorchoice()
        choice = 0
        i = 0
        switch = 0
        goatpos = random.choice(imagepositions)
        goat.setpos(goatpos)  # goat 1 randomly placed
        goat1_position = imagepositions.index(goatpos) + 1
        goatpos2 = random.choice(imagepositions)
        goat2.setpos(goatpos2)  # goat 2 randomly placed
        goat2_position = imagepositions.index(goatpos2) + 1

        if goat1_position != goat2_position:  # goat 1 and goat 2 to not be in same position
            carpos = random.choice(imagepositions)
            car.setpos(carpos)  # car randomly placed
            car_position = imagepositions.index(carpos) + 1

            if car_position != goat2_position and car_position != goat1_position:  # car and goat 2 and goat 1 to not be in same position
                d1 = goat1_position
                d2 = goat2_position
                d3 = car_position
                d11 = int(goat1_position)
                d22 = int(goat2_position)
                d33 = int(car_position)
                i += 1
                Richard_Aliaksei.setpos(-180, 113)
                for i in range(3):  # loops 3 doors
                    Richard_Aliaksei.setheading(0)
                    Richard_Aliaksei.begin_fill()
                    Richard_Aliaksei.color('black', 'yellow')
                    Richard_Aliaksei.forward(100)  # move forward (# of pixels)
                    Richard_Aliaksei.left(90)  # turn 90 degrees CW
                    Richard_Aliaksei.forward(175)
                    Richard_Aliaksei.left(90)
                    Richard_Aliaksei.forward(100)
                    Richard_Aliaksei.left(90)
                    Richard_Aliaksei.forward(175)
                    Richard_Aliaksei.left(90)
                    Richard_Aliaksei.end_fill()

                    Richard_Aliaksei.penup()
                    Richard_Aliaksei.forward(150)
                    Richard_Aliaksei.pendown()

                d1text = turtle.Turtle()
                d1text.penup()
                d1text.setpos(goatpos)
                d1text.pendown()
                d1text.write('Door {}'.format(d11), font=('Arial', 12, 'normal'))  # labeling each door in Turtle
                d1text.hideturtle()

                d2text = turtle.Turtle()
                d2text.penup()
                d2text.setpos(goatpos2)
                d2text.pendown()
                d2text.write('Door {}'.format(d22), font=('Arial', 12, 'normal'))  # labeling each door in Turtle
                d2text.hideturtle()

                d3text = turtle.Turtle()
                d3text.penup()
                d3text.setpos(carpos)
                d3text.pendown()
                d3text.write('Door {}'.format(d33), font=('Arial', 12, 'normal'))  # labeling each door in Turtle
                d3text.hideturtle()

                Richard_Aliaksei.penup()
                Richard_Aliaksei.setpos(-95, 190)  # set position of circles
                Richard_Aliaksei.pendown()

                for i in range(3):  # draws circles in Turtle
                    Richard_Aliaksei.begin_fill()
                    Richard_Aliaksei.color('black', 'green')
                    Richard_Aliaksei.circle(5)
                    Richard_Aliaksei.end_fill()

                    Richard_Aliaksei.penup()
                    Richard_Aliaksei.forward(150)
                    Richard_Aliaksei.pendown()

                dtext = turtle.Turtle()  # text of question for selection of door 1,2,3
                dtext.ht()
                dtext.penup()
                dtext.setpos(-85, 405)  # set position of text
                dtext.pendown()
                dtext.write("A guy in Wawa asks you to press 1, 2, or 3 to select your door!",
                            font=('Arial', 12, 'normal'))

                def choice1(x, y):
                    if x > -180 and x < -80 and y > 113 and y < 288:
                        d111()
                    if x > -30 and x < 70 and y > 113 and y < 288:
                        d222()
                    if x > 120 and x < 340 and y > 113 and y < 288:
                        d333()

                screen1.onclick(choice1)

                # Character number 1
                def d111():
                    choice = 1
                    dtext = turtle.Turtle()
                    dtext.penup()
                    dtext.setpos(-85, 393)
                    dtext.pendown()
                    dtext.write("You picked door number 1", font=('Arial', 12, 'normal'))
                    time.sleep(1)
                    if choice == d1:
                        dtext.penup()
                        dtext.setpos(12, )
                        dtext.pendown()
                        dtext.write("One goat is behind door {}".format(d2), font=('Arial', 12, 'normal'))
                        time.sleep(1)

                        goat3 = Turtle(G3)
                        goat3.penup()
                        goat3.setpos(goatpos2)
                        dtext.penup()
                        dtext.setpos(-85, 365)
                        dtext.ht()
                        dtext.write("Do you want to switch to door# {}. Press S for SWITCH or H for HOLD".format(d3),
                                    font=('Arial', 12, 'normal'))

                        def switchcommandy():
                            choice = d3
                            if choice == car_position:
                                car_win1()
                                carwinswitch()
                            elif choice != car_position:
                                goat_lose1()

                        def switchcommandn():
                            if choice == car_position:
                                car_win1()
                            elif choice != car_position:
                                goat_lose1()

                    elif choice == d2:
                        dtext.penup()
                        dtext.setpos(-85, 379)
                        dtext.pendown()
                        dtext.write("One goat is behind door {}".format(d1), font=('Arial', 12, 'normal'))
                        time.sleep(1)
                        goat3 = Turtle(G3)
                        goat3.penup()
                        goat3.setpos(goatpos)
                        dtext.penup()
                        dtext.setpos(-85, 365)
                        dtext.ht()
                        dtext.write("Do you want to switch to door# {}. Press S for SWITCH or H for HOLD".format(d3),
                                    font=('Arial', 12, 'normal'))

                        def switchcommandy():
                            choice = d3
                            if choice == car_position:
                                car_win2()
                            elif choice != car_position:
                                goat_lose2()

                        def switchcommandn():
                            if choice == car_position:
                                car_win2()
                            elif choice != car_position:
                                goat_lose2()

                    elif choice == d3:
                        dtext.penup()
                        dtext.setpos(-85, 379)
                        dtext.write("One goat is behind door {}".format(d1), font=('Arial', 12, 'normal'))
                        time.sleep(1)
                        goat3 = Turtle(G3)
                        goat3.penup()
                        goat3.setpos(goatpos)
                        dtext.penup()
                        dtext.setpos(-85, 365)
                        dtext.ht()
                        dtext.write("Do you want to switch to door# {}. Press S for SWITCH or H for HOLD".format(d2),
                                    font=('Arial', 12, 'normal'))

                        def switchcommandy():
                            choice = d2
                            if choice == car_position:
                                car_win2()
                            elif choice != car_position:
                                goat_lose2()

                        def switchcommandn():
                            if choice == car_position:
                                car_win2()
                            elif choice != car_position:
                                goat_lose2()

                    switchcommand.onkey(switchcommandy, "s")
                    switchcommand.onkey(switchcommandn, "h")

                # Character number 2
                def d222():
                    choice = 2
                    dtext = turtle.Turtle()
                    dtext.penup()
                    dtext.setpos(-85, 393)
                    dtext.pendown()
                    dtext.write("You picked door number 2", font=('Arial', 12, 'normal'))
                    time.sleep(1)
                    if choice == d1:
                        dtext.penup()
                        dtext.setpos(-85, 379)
                        dtext.write("One goat is behind door {}".format(d2), font=('Arial', 12, 'normal'))
                        time.sleep(1)
                        goat3 = Turtle(G3)
                        goat3.penup()
                        goat3.setpos(goatpos2)
                        dtext.penup()
                        dtext.setpos(-85, 365)
                        dtext.ht()
                        dtext.write("Do you want to switch to door# {}. Press S for SWITCH or H for HOLD".format(d3),
                                    font=('Arial', 12, 'normal'))

                        def switchcommandy():
                            choice = d3
                            if choice == car_position:
                                car_win1()
                            elif choice != car_position:
                                goat_lose1()

                        def switchcommandn():
                            if choice == car_position:
                                car_win1()
                            elif choice != car_position:
                                goat_lose1()

                    elif choice == d2:
                        dtext.penup()
                        dtext.setpos(-85, 379)
                        dtext.write("One goat is behind door {}".format(d1), font=('Arial', 12, 'normal'))
                        time.sleep(1)
                        goat3 = Turtle(G3)
                        goat3.penup()
                        goat3.setpos(goatpos)
                        dtext.penup()
                        dtext.setpos(-85, 365)
                        dtext.ht()
                        dtext.write("Do you want to switch to door# {}. Press S for SWITCH or H for HOLD".format(d3),
                                    font=('Arial', 12, 'normal'))

                        def switchcommandy():
                            choice = d3
                            if choice == car_position:
                                car_win2()
                            elif choice != car_position:
                                goat_lose2()

                        def switchcommandn():
                            if choice == car_position:
                                car_win2()
                            elif choice != car_position:
                                goat_lose2()

                    elif choice == d3:
                        dtext.penup()
                        dtext.setpos(-85, 379)
                        dtext.write("One goat is behind door {}".format(d1), font=('Arial', 12, 'normal'))
                        time.sleep(1)
                        goat3 = Turtle(G3)
                        goat3.penup()
                        goat3.setpos(goatpos)
                        dtext.penup()
                        dtext.setpos(-85, 365)
                        dtext.ht()
                        dtext.write("Do you want to switch to door# {}. Press S for SWITCH or H for HOLD".format(d2),
                                    font=('Arial', 12, 'normal'))

                        def switchcommandy():
                            choice = d2
                            if choice == car_position:
                                car_win2()
                            elif choice != car_position:
                                goat_lose2()

                        def switchcommandn():
                            if choice == car_position:
                                car_win2()
                            elif choice != car_position:
                                goat_lose2()

                    switchcommand.onkey(switchcommandy, "s")
                    switchcommand.onkey(switchcommandn, "h")

                # Character number 3
                def d333():
                    choice = 3
                    dtext = turtle.Turtle()
                    dtext.penup()
                    dtext.setpos(-85, 393)
                    dtext.pendown()
                    dtext.write("You picked door number 3", font=('Arial', 12, 'normal'))
                    time.sleep(1)
                    if choice == d1:
                        dtext.penup()
                        dtext.setpos(-85, 379)
                        dtext.pendown()
                        dtext.write("One goat is behind door {}".format(d2), font=('Arial', 12, 'normal'))
                        time.sleep(1)
                        goat3 = Turtle(G3)
                        goat3.penup()
                        goat3.setpos(goatpos2)
                        dtext.penup()
                        dtext.setpos(-85, 365)
                        dtext.ht()
                        dtext.write("Do you want to switch to door# {}. Press S for SWITCH or H for HOLD".format(d3),
                                    font=('Arial', 12, 'normal'))

                        def switchcommandy():
                            choice = d3
                            if choice == car_position:
                                car_win1()
                            elif choice != car_position:
                                goat_lose1()

                        def switchcommandn():
                            if choice == car_position:
                                car_win1()
                            elif choice != car_position:
                                goat_lose1()

                    elif choice == d2:
                        dtext.penup()
                        dtext.setpos(-85, 379)
                        dtext.pendown()
                        dtext.write("One goat is behind door {}".format(d1), font=('Arial', 12, 'normal'))
                        time.sleep(1)
                        goat3 = Turtle(G3)
                        goat3.penup()
                        goat3.setpos(goatpos)

                        dtext.penup()
                        dtext.setpos(-85, 365)
                        dtext.ht()
                        dtext.write("Do you want to switch to door# {}. Press S for SWITCH or H for HOLD".format(d3),
                                    font=('Arial', 12, 'normal'))

                        def switchcommandy():
                            choice = d3
                            if choice == car_position:
                                car_win2()
                            elif choice != car_position:
                                goat_lose2()

                        def switchcommandn():
                            if choice == car_position:
                                car_win2()
                            elif choice != car_position:
                                goat_lose2()

                    elif choice == d3:
                        dtext.penup()
                        dtext.setpos(-85, 379)
                        dtext.pendown()
                        dtext.write("One goat is behind door {}".format(d1), font=('Arial', 12, 'normal'))
                        time.sleep(1)
                        goat3 = Turtle(G3)
                        goat3.penup()
                        goat3.setpos(goatpos)
                        dtext.penup()
                        dtext.setpos(-85, 365)
                        dtext.ht()
                        dtext.write("Do you want to switch to door# {}. Press S for SWITCH or H for HOLD".format(d2),
                                    font=('Arial', 12, 'normal'))

                        def switchcommandy():
                            choice = d2
                            if choice == car_position:
                                car_win2()
                            elif choice != car_position:
                                goat_lose2()

                        def switchcommandn():
                            if choice == car_position:
                                car_win2()
                            elif choice != car_position:
                                goat_lose2()

                    switchcommand.onkey(switchcommandy, "s")
                    switchcommand.onkey(switchcommandn, "h")

                key.onkey(d111, "1")  # adds character number '1' as an input from keyboard by user
                key.onkey(d222, "2")  # adds character number '2' as an input from keyboard by user
                key.onkey(d333, "3")  # adds character number '3' as an input from keyboard by user
                key.listen()

                Play_again.penup()
                Play_again.setpos(-120, 50)
                Play_again.pendown()
                Play_again.hideturtle()

                for i in range(2):  # creates text option for either play again or exit
                    Play_again.speed(0)
                    Play_again.begin_fill()
                    Play_again.color('black', 'beige')
                    for j in range(2):
                        Play_again.forward(180)
                        Play_again.right(90)
                        Play_again.forward(40)
                        Play_again.right(90)
                    Play_again.end_fill()
                    Play_again.penup()
                    Play_again.forward(200)
                    Play_again.pendown()

                Play_again.penup()
                Play_again.setpos(-115, 25)
                Play_again.pendown()
                Play_again.write('Do you want to play again? Press y', font=('Arial', 10, 'normal'))

                Play_again.penup()
                Play_again.setpos(100, 25)
                Play_again.pendown()
                Play_again.write('Do you want to exit? Press n', font=('Arial', 10, 'normal'))
            else:
                continue
        else:
            continue

        key.listen()
    key.listen()


switchcommand.listen()
play.onkey(sim, "y")
play.onkey(exit, "n")
play.listen()
key.listen()