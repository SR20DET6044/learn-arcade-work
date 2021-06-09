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
    print("You have answered",points,"questions correctly.")
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

if answer.lower() == "hicas":
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
