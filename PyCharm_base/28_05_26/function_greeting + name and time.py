# def myGreeting1():
#     print("Good morning! Have a nice day!")
#
#
# sayGoodMorning = myGreeting1
# # sayGoodMorning()
#
#
# def myGreeting2():
#     print("Good afternoon! Have a nice day!")
#
#
# sayGoodAfternoon = myGreeting2
# # sayGoodAfternoon()
#
#
# def myGreeting3():
#     print("Good evening! Be ready to go to sleep!")
#
#
# sayGoodEvening = myGreeting3
# # sayGoodEvening()
#
#
# def myGreeting4():
#     print("Good night! Have a good dreams!")
#
# sayGoodNight = myGreeting4
# # sayGoodNight()
#
# def auhtorization(name):
#     if name == 'bob':
#         sayGoodMorning()
#     elif name == 'fish':
#         sayGoodAfternoon()
#     elif name == 'nebob':
#         sayGoodEvening()
#     else:
#         sayGoodNight()
#
#
# myGreetingsList = (myGreeting1, myGreeting2, myGreeting3, myGreeting4)
# for myGreeting in myGreetingsList:
#     myGreeting()


def myGreeting1(name):
    print(f"Good morning {name}! Have a nice day!")


def myGreeting2(name):
    print(f"Good afternoon {name}! Have a nice day!")


def myGreeting3(name):
    print(f"Good evening {name}! Be ready to go to sleep!")


def myGreeting4(name):
    print(f"Good night {name}! Have a good dreams!")


def greetingRecipient(greeting_func):
    name = input("Введите ваше имя: ")
    greeting_func(name)


def checkTimeDay():
    time = input("Введите время суток(M-morning; D-afternoon;E-evening;N-night), для выхода напишите Exit").lower()
    if time == "m":
        greetingRecipient(myGreetingsList[0])
    elif time == "d":
        greetingRecipient(myGreetingsList[1])
    elif time == "e":
        greetingRecipient(myGreetingsList[2])
    elif time == "n":
        greetingRecipient(myGreetingsList[3])
    elif time == "exit":
        print("Успешеый выход!")
        return
    else:
        checkTimeDay()


myGreetingsList = [myGreeting1, myGreeting2, myGreeting3, myGreeting4]

checkTimeDay()

# for myGreeting in myGreetingsList:
#     greetingRecipient(myGreeting)
