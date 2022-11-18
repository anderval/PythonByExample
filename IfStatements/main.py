def chlg12():
    num1 = int(input("Insert first number: "))
    num2 = int(input("Insert second number: "))

    if num1 > num2:
        print(num2, num1)
    else:
        print(num1, num2)


def chlg13():
    num = int(input("Insert a number under 20: "))

    if num >= 20:
        print("Too high")
    else:
        print("Thank you")


def chlg14():
    num = int(input("Insert a number between 10 and 20: "))

    if num >= 10 and num <= 20:
        print("Thank you")
    else:
        print("Incorrect answer")


def chlg15():
    color = input("What is your favorite colour? ")

    if color == "red" or color == "RED" or color == "Red":
        print("I like red too")
    else:
        print("I don't like", color)


def chlg16():
    answer = input("It is raining? ")

    if answer.lower() == "yes":
        answer = input("It is windy? ")

        if answer.lower() == "yes":
            print("It is too windy for an umbrella")
        else:
            print("Take an umbrella")

    else:
        print("Enjoy your day")


def chlg17():
    age = int(input("How old are you? "))

    if age >= 18:
        print("You can vote")
    elif age == 17:
        print("You can learn to drive")
    elif age == 16:
        print("You can buy a lottery ticket")
    else:
        print("You can go Trick-or-Treating")


def chlg18():
    num = int(input("Insert a number: "))

    if num >= 10 and num <= 20:
        print("Correct")
    elif num < 10:
        print("Too low")
    else:
        print("Too high")


def chlg19():
    num = int(input("Choose a option 1, 2 or 3: "))

    if num == 1:
        print("Thank you")
    elif num == 2:
        print("Well done")
    elif num == 3:
        print("Correct")
    else:
        print("Error message")


chlg19()