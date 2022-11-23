def chlg20():
    name = input("Enter your first name: ")
    print(len(name))


def chlg21():
    firstname = input("Enter your first name: ")
    name = input("Enter your last name: ")
    full_name = name + " " + surname
    print(full_name, len(full_name))


def chlg22():
    name = input("Enter your first name: ")
    surname = input("Enter your last name: ")
    name = name.title()
    surname = surname.title()
    full_name = name + " " + surname

    print(full_name)


def chlg23():
    nursery_rhyme = input("Enter a nursery rhyme: ")
    length = len(nursery_rhyme)
    start_num = int(input("Digit a starting number: "))
    end_num = int(input("Digit a end number: "))
    print(nursery_rhyme[start_num:end_num])


def chlg24():
    word = input("Enter a word: ")
    word = word.upper()
    print(word)


def chlg25():
    name = input("Enter your first name: ")
    length = len(name)
    if length < 5:
        surname = input("enter your last name: ")
        full_name = name+surname
        print(full_name.upper())
    else:
        print(name.lower())

def chlg26():
    word = input("Enter a word: ")
    if word[0].lower() == "a" or word[0].lower() == "e" or word[0].lower() == "i" or word[0].lower() == "o" or word[0].lower() == "u":
        word = word+"way"
        print(word.lower())
    else:
        word = word[1:len(word)]+"ay"
        print(word.lower())



chlg26()
