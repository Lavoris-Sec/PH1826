users = {
    'admin': '111',
    'student': '222'
}


def check_data(login, password):
    if login in users and users[login] == password:
        return True
    return False


def userLogIn(login, password):
    if check_data(login, password):
        print(f" Успешный вход! Добро пожаловать, {login}.")
    else:
        print(" Ошибка: Неверный логин или пароль!")


def changePass(login, password):
    if check_data(login, password):
        new_password = input("Введите новый пароль: ")

        users[login] = new_password
        print(f" Пароль для пользователя {login} успешно изменен!")
    else:
        print(" Ошибка: Неверный логин или старый пароль! Смена невозможна.")


def userAction(action_func):
    def run():
        login = input("Введите ваш логин: ")
        password = input("Введите ваш пароль: ")
        action_func(login, password)

    return run


while True:
    print("\n--- Меню ---")
    print("1: LogIn")
    print("2: Change password")
    print("3: Exit (Выход)")

    choice = input("Выберите действие (1-3): ")

    if choice == '1':
        action = userAction(userLogIn)
        action()
    elif choice == '2':
        action = userAction(changePass)
        action()
    elif choice == '3':
        print("Успешный выход из программы.")
        break
    else:
        print("Неверный выбор. Попробуйте еще раз.")