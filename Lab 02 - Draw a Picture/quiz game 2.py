#welcome


def welcome1():
    print("Hello! Welcome to my car quiz!")
    print()

def correct1():
    print("Correct!")
    print()

def incorrect1():
    print("Incorrect")
    print()

def completion1():
    print("You have completed the quiz!")

def score1():
    print("Your score is", percent, "percent!")


welcome1()


#name input
name = input("What is your name? ")
points = 0
questions = 0

#question 1

questions += 1

answer = input("What is the stock horsepower of the Toyota 2JZ-GTE? ")

if answer == "320":
    correct1()
    points += 1

else:
    incorrect1()

#question 2

questions += 1

answer = input("What is the abbreviation for Honda's variable valve timing system? ")

if answer.upper() == "VTEC":
        correct1()
        points += 1

else:
    incorrect1()

#question 3

questions += 1

answer = input("What is the cubic centimeter displacement of the RB20DET? ")

if answer == "1998":
    correct1()
    points += 1

else:
    incorrect1()

#question 4

questions += 1

answer = input("What is the name of the four wheel drive system found in many older Nissans? ")

if answer.upper() == "ATTESA":
        correct1()
        points += 1

else:
    incorrect1()

#question 5

questions += 1

answer = input("What is the name of the four wheel steering system found in many older Nissans? ")

if answer.upper() == "HICAS":
        correct1()
        points += 1

else:
        incorrect1()


completion1()

percent = int(points/questions*100)

score1()

if percent == 100:
    for i in range(3):
        print("Hooray!")

else:
    print("")

input("Press Enter to claim your award!")

#graphics

import arcade



arcade.open_window(600, 600, "Car")

arcade.set_background_color((arcade.csscolor.CORNFLOWER_BLUE))

arcade.start_render()

def draw_body():

    #rectangle body

    arcade.draw_rectangle_filled(300, 325, 120, 20, (201, 40, 67))

    arcade.draw_rectangle_filled(300, 330, 240, 20, (201, 40, 67))

    arcade.draw_rectangle_filled(180, 325, 20, 20, (201, 40, 67))

    arcade.draw_rectangle_filled(420, 325, 20, 20, (201, 40, 67))

    arcade.draw_rectangle_filled(300, 340, 260, 25, (201, 40, 67))

draw_body()

#polygon top body

arcade.draw_polygon_filled(((220, 320),
                            (380, 320),
                            (350, 390),
                            (250, 390),
                            ),
                           (201, 40, 67))

#windows

def draw_windows():

    arcade.draw_polygon_filled(((280, 360),
                            (355, 360),
                            (345, 380),
                            (280, 380),
                            ),
                           arcade.csscolor.LIGHT_SKY_BLUE)

    arcade.draw_polygon_filled(((245, 360),
                            (270, 360),
                            (270, 380),
                            (255, 380),
                            ),
                           arcade.csscolor.LIGHT_SKY_BLUE)

draw_windows()

def draw_wheel_arc():

    #arc over wheels

    arcade.draw_arc_filled(385, 315, 70, 25, (201, 40, 67), 0, 180)

    arcade.draw_arc_filled(215, 315, 70, 25, (201, 40, 67), 0, 180)

    arcade.draw_circle_filled(215, 295, 28, arcade.csscolor.CORNFLOWER_BLUE)

    arcade.draw_circle_filled(385, 295, 28, arcade.csscolor.CORNFLOWER_BLUE)

draw_wheel_arc()

#circle wheels

def draw_wheels():
    """Draw wheels"""
    arcade.draw_circle_filled(385, 300, 20, arcade.csscolor.DARK_SLATE_GREY)

    arcade.draw_circle_filled(215, 300, 20, arcade.csscolor.DARK_SLATE_GREY)

    arcade.draw_circle_filled(385, 300, 15, arcade.csscolor.GREY)

    arcade.draw_circle_filled(215, 300, 15, arcade.csscolor.GREY)

draw_wheels()

def draw_lights():

    #headlight

    arcade.draw_arc_filled(430, 330, 10, 20, arcade.csscolor.WHITE_SMOKE, 90, 270)

    #taillight

    arcade.draw_arc_filled(170, 330, 10, 20, arcade.csscolor.GOLDENROD, 270, 450)

draw_lights()

#door handle

arcade.draw_line(285, 345, 300, 345, arcade.color.BLACK, 2)


arcade.finish_render()

arcade.run()