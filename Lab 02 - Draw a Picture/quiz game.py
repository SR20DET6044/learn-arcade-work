#welcome

print("Hello! Welcome to my quiz!")

#name input
name = input("What is your name? ")
points = 0
questions = 0

#question 1

questions += 1

answer = input("What is 1+1? ")

if answer == "2":
    print("Correct!")
    points += 1

else:
    print("Incorrect")

#question 2

questions += 1

answer = input("What is 2+2? ")

if answer == "4":
    print("Correct!")
    points += 1

else:
    print("Incorrect")

#question 3

questions += 1

answer = input("What is 3+3? ")

if answer == "6":
    print("Correct!")
    points += 1

else:
    print("Incorrect")

#question 4

questions += 1

answer = input("What is 4+4?")

if answer == "8":
    print("Correct!")
    points += 1

else:
    print("Incorrect")

#question 5

questions += 1

answer = input("What is 5+5?")

if answer == "10":
        print("Correct!")
        points += 1

else:
        print("Incorrect")

#question 6

questions += 1

answer = input("What is the capital of Japan? ")

if answer.lower() == "tokyo":
        print("Correct!")
        points += 1

else:
        print("Incorrect")

#question 6

questions += 1

answer = input("What is the capital of France? ")

if answer.upper() == "PARIS":
        print("Correct!")
        points += 1

else:
        print("Incorrect")


print("You have completed the quiz!")

print("Your score is", int(points/questions*100), "percent!")