# def_name = input("Введите ваше имя - ")
# choice = 0
#
# def upp_low(name, action):
#     if action == 1:
#         uppp(name)
#     if action == 2:
#         loww(name)
#
#
# def uppp(name_fot_up):
#     print(f"user{name_fot_up.upper()}")
#
#
# def loww(name_for_low):
#     print(f"user{name_for_low.lower()}")
#
#
# while choice not in ['1', '2']:
#     choice = input(
#         f"В каком регистре добавить ваше имя?\n---Верхний регистр - user{def_name.upper()}--- 1\n"
#         f"--- Нижний регистр - user{def_name.lower()}--- 2\n")
#     if choice not in ['1', '2']:
#         print("Неверный ввод")
#     else:
#         print('Успешный выбор')
#         upp_low(def_name, int(choice))


def nameUpper(name):
    return "user" + name.upper()


def nameLower(name):
    return "user" + name.lower()


def makeLog(userName, maker):
    return maker(userName)


def_name = input("Введите ваше имя - ")
choice = 0

while True:
    choice = input(
        f"В каком регистре добавить ваше имя?\n"
        f"--- Верхний регистр - {nameUpper(def_name)} --- 1\n"
        f"---  Нижний регистр - {nameLower(def_name)} --- 2\n"
    )

    result = "Неверный формат, повторите попытку"
    if choice == '1':
        result = makeLog(def_name, nameUpper())
    elif choice == '2':
        result = makeLog(def_name, nameLower())
    print(result)

    # if choice in ['1', '2']:
    #     print("Успешный выбор")
    #
    #     if int(choice) == 1:
    #         selected_maker = nameUpper
    #     else:
    #         selected_maker = nameLower
    #
    #     login = makeLog(def_name, selected_maker)
    #
    #     print(f"Ваш логин: {login}")
    #     break
    #
    # print("↑↑↑ Неверный ввод\n")
