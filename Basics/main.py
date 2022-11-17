def chlg1():
    firstname = input("What is your first name?")
    print("Hello", firstname)


def chlg2():
    first_name = input("What is your first name?")
    last_name = input("What is your last name?")
    print("Hello", first_name, last_name)


def chlg3():
    print("What do you call a bear with no teeth?\nA gummy bear!")


def chlg4():
    num1 = int(input("Insert first number: "))
    num2 = int(input("Insert second number: "))
    print("The total is ", num1 + num2)


def chlg5():
    num1 = int(input("Insert first number: "))
    num2 = int(input("Insert second number: "))
    num3 = int(input("Insert third number: "))

    total = (num1 + num2) * num3

    print("The answer is ", total)


def chlg6():
    pizza_slices_started = int(input("How many slices of pizza did it come in? "))
    pizza_slices_eat = int(input("How many slices of pizza did you eat? "))

    print(pizza_slices_started - pizza_slices_eat, "slices of pizza left.")


def chlg7():
    name = input("What is your name? ")
    age = int(input("How old are you? "))

    print(name, "next birthday you will be", age + 1)


def chlg8():
    total_price = float(input("What is total price of the bill? "))
    people = int(input("How many people will split the bill? "))
    print("Each person will pay", total_price / people)


def chlg9():
    days = int(input("Number of days: "))
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60

    print(days, "days\n", hours, "hours\n", minutes, "minutes\n", seconds, "seconds\n")


def chlg10():
    weight_kilos = float(input("What is your weight in kilos? "))
    weight_pounds = weight_kilos*2.204
    print("Your weight in pounds is", weight_pounds)


def chlg11():
    larger_num = int(input("Insert a number over 100: "))
    smaller_num = int(input("Insert a number under 10: "))
    into_num = larger_num/smaller_num

    print("The number", smaller_num, "fits into the number", larger_num, ",", into_num, "times")


chlg11()
