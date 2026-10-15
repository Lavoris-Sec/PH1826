# def some_fn(*args):
#     quantity = 0
#     args_sum = 0
#     for arg in args:
#         quantity += 1
#         args_sum += arg
#     return args_sum/quantity
#
# print(some_fn(1, 2, 3))


# Необходимо написать функцию, которая выводит логин и пароль пользователя (каждый из них с новой строки)
# согласно некоторому шаблону
# Набор исходных данных — это вложенный список (набор логинов и паролей нескольких пользователей):
# users=[['user1', '111'],
#  ['user2', '2222'],
#  ['user3', '33333']]
a = "↓↓↓"
# def printer(users_list):
#     for i in range(len(users_list)):
#         if len(users_list[i]) == 1:
#             users_list[i].append("дефолтный_пароль")
#
#     for login, password, *_ in users_list:  # *_ для переменных которые не нужны
#         print(f"login: {login}\npassword: {password}\n")
#
#         # print("login: {0}\npassword: {1}".format(login, password))
#
#
# users = [['user1', '111'],
#          ['user2', '2222'],
#          ['user3', '3333']]
#
# printer(users)
a_ = "↑↑↑"

# Пример Сергея
b = " ↓↓↓"
# def printInfo(*clients):
#     for i in range(len(clients)):
#         if i == 0:
#             print("login: {}".format(clients[i]))
#         elif i == 1:
#             print("pass: {}".format(clients[i]))
# for user in users:
#     printInfo(*user)
b_ = "↑↑↑"


def userGreetings(user, def_password ="111"):
    user = user.lower()
    if user == 'admin':
        print("Hello admin")
    elif user == 'manager':
        print("You manager, work harder")
    elif user == 'teacher':
        print("Teach better")
    else:
        print("We don`t know you, get out")
    print("")
    print(login, " - ", def_password)


login = input("login - ")
password = input("password - ")
if password == "":
    password = "111"

print(login)

userGreetings(login, password)
userGreetings("admin","12345")
userGreetings("student")