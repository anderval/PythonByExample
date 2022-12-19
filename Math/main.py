import math


def chlg27():
    num = float(input("Enter a number with lots of decimal places"))
    print(num*2)


def chlg29():
    num = int(input("Enter an integer that is over 500"))
    print(round(math.sqrt(num), 2))


def chlg30():
    print(round(math.pi), 5)


def chlg21():
    num = int(input("Enter the radius of a circle"))
    area = math.pi*(num**2)
    print(round(area, 2))


chlg21()

