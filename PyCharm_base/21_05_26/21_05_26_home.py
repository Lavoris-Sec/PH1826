def calculateExample1(a, b):
    return a ** b + 2 * a - b / 0.23


def calculate_example2(a, b):
    return a * b - 5 ** a + b


def calculateExample3(a, b):
    return b ** 4 + a ** 2 - a / b


def userChoise(choise):
    x = 2
    y = 3
    if choise == '1':
        print(calculateExample1(x, y))
    elif choise == '2':
        print(calculate_example2(x, y))
    elif choise == '3':
        print(calculateExample3(x, y))
    else:
        print("↓↓↓")


input_user = input("Выберите функцию")
userChoise(input_user)
